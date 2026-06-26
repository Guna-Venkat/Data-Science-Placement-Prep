# LRU Cache

**Pattern:** Data Structure Design (Hash Map + Doubly Linked List)

**Recognition:**
- Implement Least Recently Used (LRU) cache operations (`get` and `put`) in $O(1)$ time complexity.
- Hash Map provides fast key lookup to Node references.
- Doubly Linked List (DLL) tracks access frequency: new/accessed elements are moved to the head, and elements at the tail are evicted when size exceeds capacity.

**Optimal Code (Python):**
```python
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # maps key -> Node
        # Dummy sentinel head and tail nodes to avoid edge pointer checks
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Helper to remove an existing node from the list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node: Node) -> None:
        """Helper to insert node right after head (most recently used)."""
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node location
            self._remove(self.cache[key])
            
        new_node = Node(key, value)
        self._add(new_node)
        self.cache[key] = new_node
        
        if len(self.cache) > self.capacity:
            # Evict the least recently used element (right before tail sentinel)
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]
```

**Killer Edge:**
- Cache capacity is `1` (eviction happens on every new key put if not duplicate).
- Overwriting an existing key with a new value (must update cache mapping and list ordering).

**Mistake:**
- Removing node from DLL but forgetting to delete its entry from the Hash Map dictionary (`del cache[lru_node.key]`), leading to a memory leak and capacity limit failure.
- Creating cyclic references in DLL node pointers during inserts/deletes, causing infinite loops during traversal.
