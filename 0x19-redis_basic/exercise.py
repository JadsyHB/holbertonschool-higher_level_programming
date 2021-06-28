#!/usr/bin/env python3
"""
redis module
"""


from typing import Union, Callable, Optional, Any
import redis
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """
    count Cache insts
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapped"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    """
    Cache class
    modules: init
    """
    def __init__(self):
        """
        initialization
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store function
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
        fn: Optional[Callable] = None) -> Union[str, int, bytes, float]:
        """
        get function
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data
