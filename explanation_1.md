For designing LRU with O(1) complexity. It's best to go with dictionary because of its constant time access.
And used python's `deque` to track the enties into the cache.

Becuase of the `dictionary` and `deque`, we'are able to get `O(1)` time complexity.
Space complexity: O(capacity_given)