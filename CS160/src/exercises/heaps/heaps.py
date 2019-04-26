#!/usr/bin/env python3
"""
Isaac List - CS160
April 26, 2019

Limited size max Binary Heap implementation
"""


class BinaryHeapMax:
    """Heap class implementation"""

    def __init__(self, limit: int = 0):
        self.heap = []
        self.size = 0
        self.max_size = limit
        self.smallest = None

    def perc_up(self, cur_idx):
        """Moving a node up"""
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx -1) //2
            if self.heap[cur_idx] > self.heap[parent_idx]:
                self.swap(cur_idx, parent_idx)
            else:
                return
            cur_idx = parent_idx

    def perc_down(self, cur_idx):
        """Moving a node down"""
        while 2 * cur_idx + 1 <= self.size:
            max_child_idx = self.get_max_child(cur_idx)
            if self.heap[cur_idx] < self.heap[max_child_idx]:
                self.swap(cur_idx, max_child_idx)
            else:
                return
            cur_idx = max_child_idx

    def insert(self, item):
        """Adding a new item"""
        self.heap.append(item)
        self.size += 1
        self.perc_up(self.size - 1)

    def heapify(self, not_a_heap):
        """Turning a list into a heap"""
        self.heap = [] + not_a_heap[:]
        self.size = len(not_a_heap)
        cur_idx = self.size // 2 - 1
        while cur_idx >= 0:
            self.perc_down(cur_idx)
            cur_idx = cur_idx - 1

    def get_max_child(self, parent_idx):
        """Getting a larger child"""
        raise NotImplementedError

    def __len__(self):
        """Get heap size"""
        return self.size

    def __str__(self):
        return str(self.heap)
