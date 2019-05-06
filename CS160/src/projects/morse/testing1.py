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

    def preorder(self):
        """Pre-order tree traversal"""
        print(self._key, end=" ")
        if self._child_left:
            self._child_left.preorder()
        if self._child_right:
            self._child_right.preorder()

    def inorder(self):
        """In-order tree traversal"""
        if self._child_left:
            self._child_left.inorder()
        print(self._key, end=" ")
        if self._child_right:
            self._child_right.inorder()

    def postorder(self):
        """Post-order tree traversal"""
        if self._child_left:
            self._child_left.postorder()
        if self._child_right:
            self._child_right.postorder()
        print(self._key, end=" ")

tree = BinaryTree(None)
code = ".-"
letter = "a"
current = tree
for char in code:
    if char == ".":
        left = tree.get_child_left()
        if left == None:
            current.insert_left("")
        current = current.get_child_left()
    elif char == "-":
        right = current.get_child_right()
        if right == None:
            current.insert_right("")
        current = current.get_child_right()
    current = ""


def build_tree_oop() -> object:
    """Build a tree and return it"""
    tree_oop = BinaryTree("a")
    # Left Sub-Tree
    tree_oop.insert_left("b")
    tree_oop.get_child_left().insert_right("d")
    # Right Sub-Tree
    tree_oop.insert_right("c")
    tree_oop.get_child_right().insert_left("e")
    tree_oop.get_child_right().insert_right("f")
    # Return the Tree
return tree_oop