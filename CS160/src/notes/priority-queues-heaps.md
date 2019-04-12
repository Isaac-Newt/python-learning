<i>
Isaac List

CS160 - Priority Queues with Binary Heaps

April 12, 2019
</i>

# Definitions

### Queue

- FIFO/LILO operation
- Items maintain order

### Priority Queue

- Similar to Queue (Dequeue items from front of structure)
- Nodes filled in left to right on lowest level

### Heap

- Greatest (or least) item is on top, repeated recursively for subtrees
- No rule like in binary-search tree wherein less on left / greater on right
- Minimum heap used most in class, will have exercise to build a max heap

# Binary Heap Operations

- BinaryHeap()
    - Create new empty binary heap object
- build_heap(list)
    - build new heap from list of keys
    - heapify()
- Is_empty()
- size()
- insert(item)
    - push()
    - O(log n) complexity
- Find_min()
    - peek()
    - O(1) complexity (Assuming min heap)
- Del_min()
    - pop()
    - O(log n) complexity (bigger than find, because heap must be rebuilt
    
# Implementation

### Python Heap Queue Module

```python
import heapq
list = [3, 5, 2, 6, 7, 7, 3, 6, 10, 5]
heapq.heapify(list) --> [2, 5, 3, 6, 5, 7, 3, 6, 10, 7]
```

- Minimum heap (smallest item on top recursively
- Default python operation

index | left | right
---|---|---
0 | 1 | 2
1 | 3 | 4
2 | 5 | 6
3 | 7 | 8
k | 2k+1 | 2k+2







