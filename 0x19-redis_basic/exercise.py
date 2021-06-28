#!/usr/bin/env python3
"""
redis module
"""


from typing import Union, Callable, Optional, Any
import redis
from uuid import uuid4
from functools import wraps


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

def call_history(method: Callable) -> Callable:
    """call history"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper"""
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(data))
        return data
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

    @call_history
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

    def get_int(self, key: str) -> int:
        """change to int"""
        data = self._redis.get(key)
        try:
            data(value.decode("utf-8"))
        except Exception:
            data = 0
        return data

    def get_str(self, key: str) -> str:
        """change to str"""
        data = self._redis.get(key)
        return data.decode("utf-8")


def replay(method: Callable):
    """display history"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    r = method.__self__._redis
    count = r.get(key).decode("utf-8")
    inList = r.lrange(inputs, 0, -1)
    outList = r.lrange(outputs, 0, -1)
    zipp = list(zip(inList, outList))
    print("{} was called {} times".format(key, count))
    for i, j in zipp:
        a, b = i.decode("utf-8"), j.decode("utf-8")
        print("{}(*{}) -> {}".format(key, a, b))
