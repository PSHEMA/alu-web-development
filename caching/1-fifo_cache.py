#!/usr/bin/python3
""" FIFO Caching Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Caching Class
    """
    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if (
            len(self.cache_data) >= BaseCaching.MAX_ITEMS
            and key not in self.cache_data
        ):
            first_key = next(iter(self.cache_data))
            print("DISCARD: {}".format(first_key))
            del self.cache_data[first_key]

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
