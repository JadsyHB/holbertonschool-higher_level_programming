#!/usr/bin/python3
"""
fifocache
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFO
    """
    def __init__(self):
        """init"""
        super().__init__()
        self.data = {}
        self.next_in, self.next_out = 0, 0

    def put(self, key, item):
        """put"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self._push(key, item)

    def get(self, key):
        """get"""
        if key and self.cache_data.get(key):
            return self.cache_data[key]
        return None

    def _push(self, key, item):
        """FIFO Push"""
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.data[self.next_out + 1]))
            self._pop()
        self.cache_data[key] = item
        self.next_in += 1
        self.data[self.next_in] = key

    def _pop(self):
        """ FIFO pop"""
        self.next_out += 1
        key = self.data[self.next_out]
        del self.data[self.next_out], self.cache_data[key]
