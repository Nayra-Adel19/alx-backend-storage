#!/usr/bin/env python3
"""Inside get_page track how many times particular URL"""
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
"""Inside get_page track how many times particular URL"""


def data_cacher(method: Callable) -> Callable:
    """Inside get_page track how many times particular URL"""
    @wraps(method)
    def invoker(url) -> str:
        """Inside get_page track how many times particular URL"""
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    """Inside get_page track how many times particular URL"""
    return requests.get(url).text
