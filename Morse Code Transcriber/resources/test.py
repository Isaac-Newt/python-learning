from binary_tree import BinaryTree

test_tree = BinaryTree("a")
root = test_tree.get_root_val()
print("tree root: ", root)

test_file = open("morse.txt", "r")
line = test_file.readline()
print(line)