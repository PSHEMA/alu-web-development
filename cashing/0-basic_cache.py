#!/usr/bin/python3
""" Basic dictionary """


BaseCaching = __import__('base_Cashing').BaseCaching


class BasicCache(BaseCaching):
    """ Basic dictionary caching module """

    def put(self, key, item):
        """ Add an item in the cache """

        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
