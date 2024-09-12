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
        self.lru_keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.lru_keys.remove(key)

        self.cache_data[key] = item
        self.lru_keys.append(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.lru_keys.pop(0)
            print("DISCARD: {}".format(lru_key))
            del self.cache_data[lru_key]

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
