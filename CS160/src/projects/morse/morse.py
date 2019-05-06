"""Morse code encoding and decoding"""
#!/usr/bin/env python3
# encoding: UTF-8


from src.notes.trees.BinaryTree import BinaryTree


class Coder:
    """Morse Code Encoder/Decoder"""

    def __init__(self, file_in: str):
        """Constructor"""
        morse_tree = BinaryTree(None)
        input_file = open(file_in, "r")
        for line in input_file:
            # Get the line
            line = line.strip()
            print(line)

            # Split into letter and code
            letter_code = line.split()
            letter = letter_code[0]
            code = letter_code[1]
            current_node = morse_tree
            for char in code:
                # Place the letter in its spot based on the code
                if code.index(char) == (len(code) + 1):
                    if char == ".":
                        print("left")
                        current_node.set_child_left(letter)
                    elif char == "-":
                        print("right")
                        current_node.set_child_right(letter)
                else:
                    if char == ".":
                        print("left")
                        left = current_node.get_child_left()
                        if left == None:
                            morse_tree.set_child_left("")
                        current_node = current_node.get_child_left()
                    elif char == "-":
                        print("right")
                        right = current_node.get_child_right()
                        if right == None:
                            morse_tree.set_child_right("")
                        current_node = current_node.get_child_right()

    def follow_and_insert(self, code_str: str, letter: str):
        """Follow the tree and insert a letter"""
        raise NotImplementedError

    def follow_and_retrieve(self, code_str: str):
        """Follow the tree and retrieve a letter"""
        current_node = morse_tree 
        for char in code_str:
            if char == ".":
                print("left")
                current_node = current_node.get_child_left()
            if char == "-":
                print("right")
                current_node = current_node.get_child_right()
        return current_node

    def find_path(self, tree: object, letter: str, path: str):
        """Find a key"""
        raise NotImplementedError

    def encode(self, msg: str):
        """Encode a message"""
        encoded_string = ""
        for char in msg:
            find_path(morse_tree, char, path)
        return encoded_string

    def decode(self, code: str):
        """Decode a message"""
        code_strings = code.split()
        message = ""
        for code in code_strings:
            letter = follow_and_retrieve(code)
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
