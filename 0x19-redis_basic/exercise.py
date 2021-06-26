#!/usr/bin/env python3
"""
redis module
"""


import redis
import uuid


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
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
