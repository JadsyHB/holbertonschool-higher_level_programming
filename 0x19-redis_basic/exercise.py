#!/usr/bin/env python3
""" Writing strings to Redis, Reading from Redis and recovering original type,
    Incrementing values, Storing lists, Retrieving lists """
from typing import Union, Callable, Optional, Any
import redis
import uuid
from functools import wraps


class Cache:
    """ class """
    def __init__(self):
        """ constructor - store an instance of the Redis client as a private
        variable named _redis and flush the instance using flushdb """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ generate a random key (e.g. using uuid), store the input data in
        Redis using the random key and return the key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key