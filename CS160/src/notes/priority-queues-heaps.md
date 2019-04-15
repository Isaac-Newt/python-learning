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
# import
import heapq

# Create a heap (essentially a sorted list TBH)
list = [3, 5, 2, 6, 7, 7, 3, 6, 10, 5]
heapq.heapify(list) # --> [2, 5, 3, 6, 5, 7, 3, 6, 10, 7]

# Methods
heapq.heappush(list, 1)
heapq.heappop(list)
```
```python
# Manual Heap Implementation
class BinHeap:
    def __init__(self):
        # Textbook initializes this with [0], and ignores the 0
        # We will not do that in class, simply use 0-indexed list
        # Like civilized people :)
        self.heap = []
        self.size = 0

    def sift_up(self, cur_idx):
        # New item must "sift up", i.e. swap with its parent if
        # item is smaller (is a log n operation, which is good)
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self.heap[cur_idx] < self.heap[parent_idx]:
                self.swap(cur_idx, parent_idx)
            cur_idx = parent_idx
    
    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.perc_up(self.size - 1)

    def perc_down(self, )
        while 2 * cur_idx + 1 <= self.size:
            min_child_idx = self.get_min_child(cur_idx)
            if self.heap[cur_idx] > self.heap[min_child_idx]:
                self.swap(cur_idx, min_child_idx)
            else:
                return
            cur_idx = min_child_idx

    def delete(self):
        res = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heap.pop()
        self.perc_down(0)
        return res

    def heapify(self, not_a_heap):
        self.heap = [] + not_a_heap[:]
        self.size = len(not_a_heap)
        cur_idx = self.size // 2 - 1
        while cur_idx >= 0:
            self.perc_down(cur_idx)
            cur_idx += 1
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







