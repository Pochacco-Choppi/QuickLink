from aiohttp import web
import aiohttp_jinja2

from utils import is_valid_url, create_short_unique_string
from errors import WRONG_URL_FORMAT, SOMETHING_GOES_WRONG
from settings import GENERATION_KEY_RETRIES_COUNT

routes = web.RouteTableDef()


@routes.get('/', name='index')
async def index(request):
    context = dict()
    response = aiohttp_jinja2.render_template("index.html", request, context=context)
    return response


@routes.post('/')
async def shortyfy(request):
    retries_count = 0
    context = dict()
    context['errors'] = list()
    if request.method == 'POST':
        long_url = (await request.post())['long_url']
        if not is_valid_url(long_url):
            context['errors'].append(WRONG_URL_FORMAT)
        else:
            short_key = create_short_unique_string()
            while await request.app['redis'].get(short_key) and retries_count != GENERATION_KEY_RETRIES_COUNT:
                short_key = create_short_unique_string()
                retries_count += 1
                if retries_count == GENERATION_KEY_RETRIES_COUNT:
                    context['errors'].append(SOMETHING_GOES_WRONG)
            await request.app['redis'].set(short_key, long_url)

            short_url = request.host + "/" + short_key
            context['short_url'] = short_url
            context['short_key'] = short_key

    response = aiohttp_jinja2.render_template("index.html", request, context=context)
    return response


@routes.get('/{short_id}')
async def redirect(request):
    context = dict()
    context['short_id'] = request.match_info.get("short_id", "")
    redirect_url = await request.app['redis'].get(context['short_id'])

    if redirect_url:
        return web.HTTPFound(str(redirect_url.decode()))

    return web.HTTPNotFound()
