#!/usr/bin/env python3
"""
redis module
"""


import redis
from uuid import uuid4


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
