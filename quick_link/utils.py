import uuid
import os
import re

from redis import asyncio as aioredis


def redis_config_from_env():
    config = {
        'user': os.environ["REDIS_USER"],
        'password': os.environ["REDIS_PASSWORD"],
        'host': os.environ["REDIS_HOST"],
        'port': os.environ["REDIS_PORT"],
    }
    return config


async def init_redis(conf):
    conn_str = f"redis://{conf['user']}:{conf['password']}@{conf['host']}:{conf['port']}"

    redis = await aioredis.from_url(
        conn_str,
    )
    return redis


def is_valid_url(url):
    pattern = re.compile(r'^https?://[\w\-]+(\.[\w\-]+)+[/#?]?.*$')
    return bool(pattern.match(url))


def create_short_unique_string():
    random_string = str(uuid.uuid4()).replace('-', '')[:6]
    return random_string
