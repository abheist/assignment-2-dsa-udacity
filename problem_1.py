from collections import deque


class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.key_orders = deque()

    def get(self, key):
        if key is None:
            return -1
        return self.cache.get(key, -1)

    def set(self, key, value):
        if len(self.key_orders) >= self.capacity:
            del self.cache[self.key_orders.popleft()]
        self.key_orders.append(key)
        self.cache[key] = value


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
our_cache.get(3)
