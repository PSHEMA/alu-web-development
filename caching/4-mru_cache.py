#!/usr/bin/python3
""" MRU caching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU caching system
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if (
            len(self.cache_data) >= BaseCaching.MAX_ITEMS and 
            key not in self.cache_data
        ):
            mru_key = next(reversed(self.cache_data))
            print("DISCARD: {}".format(mru_key))
            del self.cache_data[mru_key]

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
