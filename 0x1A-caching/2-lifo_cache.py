#!/usr/bin/python3
""" LIFO caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO """
    def __init__(self):
        super().__init__()
        self.last = ''

    def put(self, key, item):
        """put"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last))
                self.cache_data.pop(self.last)
            self.last = key

    def get(self, key):
        """get"""
        if key and self.cache_data.get(key):
            return self.cache_data[key]
        return None
