import asyncio
import os

from aiohttp import web
import aiohttp_jinja2
import jinja2

from routes import setup_routes
from utils import init_redis, redis_config_from_env
from settings import config


async def setup_redis(app):
    redis_config = redis_config_from_env()
    redis = await init_redis(redis_config)
    app['redis'] = redis
    return redis


async def init():
    app = web.Application()
    aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader(os.path.join(os.getcwd(), "templates"))
    )
    app['config'] = config
    await setup_redis(app)
    setup_routes(app)
    host, port = config['host'], config['port']

    return app, host, port


def main():
    loop = asyncio.get_event_loop()
    app, host, port = loop.run_until_complete(init())
    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    main()
