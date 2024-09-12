#!/usr/bin/python3
""" LRU Caching Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU Caching Class
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_recently_used = min(self.cache_data, key=self.cache_data.get)
            print("DISCARD: {}".format(least_recently_used))
            del self.cache_data[least_recently_used]

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
