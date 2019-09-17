import fileinput

class BinaryTree:
    """Binary Tree implementation as nodes and references"""

    def __init__(self, key):
        self._key = key
        self._child_left = None
        self._child_right = None

    def get_root_val(self):
        """Get root key value"""
        return self._key

    def set_root_val(self, new_key):
        """Set root key value"""
        self._key = new_key

    def get_child_left(self):
        """Get left child"""
        return self._child_left

    def set_child_left(self, new_child_left):
        """Set left child"""
        self._child_left = new_child_left

    def get_child_right(self):
        """Get right child"""
        return self._child_right

    def set_child_right(self, new_child_right):
        """Set right child"""
        self._child_right = new_child_right

    def is_leaf(self):
        """Check if a node is leaf"""
        return (not self._child_left) and (not self._child_right)

    def insert_left(self, new_node):
        """Insert left subtree"""
        new_subtree = BinaryTree(new_node)
        if self._child_left != None:
            new_subtree.set_child_left(self._child_left)
        self._child_left = new_subtree

    def insert_right(self, new_node):
        """Insert right subtree"""
        new_subtree = BinaryTree(new_node)
        if self._child_right != None:
            new_subtree.set_child_right(self._child_right)
        self._child_right = new_subtree

    def clockwise(self):
        """Clockwise tree traversal"""
        print(self._key, end=" ")
        if self._child_right:
            self._child_right.clockwise()
        if self._child_left:
            self._child_left.clockwise()


def build_tree(tree, list, index, level) -> object:
    """Build a tree and return it"""

    # Create left and right children
    tree.set_child_left(list[(2 * index) + 1])
    tree.set_child_right(list[(2 * index) + 2])

    # Build left and right sub-trees recursively
    # TODO the int added to index is context-sensitive, not absolute
    build_tree(tree, list, index + 100000)
    build_tree(tree, list, index + 200000)

    # Return the Tree
    return tree

for line in fileinput.input():
    # Prepare input
    line = line.strip()
    list = line.split()

    # Define variables
    height = list[0]
    directions = list[1]
    number_of_nodes = (2 ** (height + 1)) - 1

    # Build a list of the numbers in reverse order
    list = []
    number = number_of_nodes
    while number > 0:
        list.add(number)

    # Create the tree
    tree = BinaryTree(list[0])
    final_tree = build_tree(tree, list, 0, 0)