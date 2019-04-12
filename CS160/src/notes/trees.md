<i>Isaac List - CS160 

April 10, 2019

Tree data structure</i>


## Operations on Trees
- insertion
    - if binary tree (or balanced)
- printing a binary tree
    - recursively print root-left-right (or left-right-root or right-left-root or root right-left)
    - Simply print in order level-by-level

# Characteristics of Trees

## Applications
- Operating systems
- Networking
- Databases

## Examples
- DOM (html)
- File system
- Animal classification

## Structure
- Root (top item, no incoming edges)
- Branches (sub-trees)
- Leaves (Nodes with no children)
- Node (Can have a name, payload)
- Edge (connection between two nodes)
- Path (ordered list of nodes connected by edges)
- Children (Incoming edges)
- Parents (Node with children (outgoing edges))
- Siblings (Nodes that share same parent)
- Level (Number of edges on path from root to node <i>n</i>)
- Height (Max level of any node in the tree)

## Traversal

### How to print values in a predetermined order

## <i>!!! Never right before left !!!</i>

- Preorder Method
    - Visit root node first
    - recursive preorder traversal of left subtree
    - recursive preorder traversal of right subtree

    ```python
    def preorder(tree):
    """Python example of a preorder tree traversal"""
        if tree:
            print(tree.get_root_val())
            preorder(tree.get_child_left())
            preorder(tree.get_child_right())
    ```

- Inorder

    ```python
    def inorder(self):
        print(self.root)
        if self.child_left:
            self.child_left.inorder()
        if self.child_right:
            self.child_right.inorder()

# Implementation

## Trees as lists of lists

```python
my_tree = ['a',              # root
          ['b',              # left sub-tree
            ['d', [], []],
            ['e', [], []] ],
          ['c',              # right sub-tree
            ['f', [], []],
            [] ]
          ]
```

### Issues with this:
- Not very effective when scaled up (cumbersome)

---

## Trees as nodes and references 

### Similar to linked lists, just with more "next" node(s)

```python
class Node:
"""Create a node for a Tree structure"""
    def __init__(self, data):
    """"""
        self._data = data
        self._left = None
        self._right = None
```