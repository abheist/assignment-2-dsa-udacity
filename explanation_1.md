For designing LRU with O(1) complexity. It's best to go with dictionary because of its constant time access.
And used python's `deque` to track the enties into the cache.

Becuase of the `dictionary` and `deque`, we'are able to get `O(1)` time complexity.
Space complexity: O(capacity_given) - In the worst case the cache will be full with the given capacity. Though the cache will never exceed the given capacity as we are removing the Least Recently used value when the cache gets full.