"""
Isaac List - CS160
May 8, 2019

Morse code encoding and decoding
"""
#!/usr/bin/env python3
# encoding: UTF-8


# from src.notes.trees.BinaryTree import BinaryTree
from pythonds3.trees import BinaryTree

class Coder:
    """Morse Code Encoder/Decoder"""

    def __init__(self, file_in: str):
        """Constructor"""
        self.morse_tree = BinaryTree("")
        input_file = open(file_in, "r")
        for line in input_file:
            # Get the line
            line = line.strip()

            # Split into letter and code
            letter_code = line.split()
            letter = letter_code[0]
            code = letter_code[1]

            # Add letter to the tree
            self.follow_and_insert(code, letter)

    def follow_and_insert(self, code_str: str, letter: str):
        """Follow the tree and insert a letter"""

        # Set current node to the tree root
        current_node = self.morse_tree

        # For each character in the code, move to the left or right child
        for char in code_str:
            if char == ".":
                # If child doesn't exist, create an empty node
                if current_node.get_child_left() == None:
                    current_node.insert_left("")
                # Move the current node
                current_node = current_node.get_child_left()
            elif char == "-":
                # If child doesn't exist, create an empty node
                if current_node.get_child_right() == None:
                    current_node.insert_right("")
                # Move the current node
                current_node = current_node.get_child_right()

        current_node.set_root_val(letter)

    def follow_and_retrieve(self, code_str: str):
        """Follow the tree and retrieve a letter"""
        current_node = self.morse_tree 
        for char in code_str:
            if current_node == None:
                return None
            else:
                if char == ".":
                    current_node = current_node.get_child_left()
                if char == "-":
                    current_node = current_node.get_child_right()
        if current_node != None:
            return current_node.get_root_val()
        else:
            return None

    def find_path(self, tree: object, letter: str, path: str):
        """Find a key"""
        error = f"Could not encode {letter}: {letter} is not in the tree"
        left_tree = tree.get_child_left()
        right_tree = tree.get_child_right()

        if left_tree == None:
            raise ValueError(error)
        elif left_tree.get_root_val() == letter:
            path += "."
            return path
        elif right_tree == None:
            raise ValueError(error)
        elif right_tree.get_root_val() == letter:
            path += "-"
            return path
        else:
            left_path = path + "."
            right_path = path + "-"
            try:
                return self.find_path(left_tree, letter, left_path)
            except:
                return self.find_path(right_tree, letter, right_path)
        

    def encode(self, msg: str):
        """Encode a message"""
        encoded_string = ""
        for char in msg:
            if char == " ":
                encoded_string = encoded_string
            else:
                path = ""
                path = self.find_path(self.morse_tree, char, path)
                encoded_string = encoded_string + path + " "
        return encoded_string

    def decode(self, code: str):
        """Decode a message"""
        code_strings = code.split()
        message = ""
        for code in code_strings:
            letter = self.follow_and_retrieve(code)
            if letter == None:
                error = f"Could not decode {code}: {code} is not in the tree"
                raise ValueError(error)
            message += letter
        return message


def main():
    morse_coder = Coder("data/projects/morse/morse.txt")
    print("Encoding 'sos'")
    print("Expected: ... --- ...")
    print("Encoded : {}".format(morse_coder.encode("sos")))
    print("---")
    print("Encoding 'data structures'")
    print("Expected: -.. .- - .- ... - .-. ..- -.-. - ..- .-. . ... ")
    print("Encoded : {}".format(morse_coder.encode("data structures")))
    print("---")
    print("Encoding '$$'")
    print("Expected: Error message")
    try:
        print("Encoded : {}".format(morse_coder.encode("$$")))
    except ValueError as ve:
        print("ERROR: {}".format(ve))
    print("---")
    print("Decoding '.... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----'")
    print("Expected: hello,cs160")
    test_str = ".... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----"
    print("Decoded : {}".format(morse_coder.decode(test_str)))


if __name__ == "__main__":
    main()
