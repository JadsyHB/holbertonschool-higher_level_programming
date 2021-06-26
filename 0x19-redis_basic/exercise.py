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

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store function
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
