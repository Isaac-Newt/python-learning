#!/usr/bin/env python3
"""Stack exercise"""

from pythonds3.basic import Stack


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class TokenError(Exception):
    """Token errors"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def rev_string(my_str):
    """Reverse characters in a string using a stack"""
    stack = Stack()
    new_str = ""
    # Add characters to stack
    for char in my_str:
        stack.push(char)
    # Pop characters out of stack into new string
    while not stack.is_empty():
        new_str += stack.pop()
    return new_str


def par_checker(line):
    """Textbook implementation"""
    stack = Stack()
    balanced = True
    i = 0
    while i < len(line) and balanced:
        symbol = line[i]
        if symbol == "(":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()
        i = i + 1
    return balanced and stack.is_empty()


def par_checker_ext(line):
    """Check if parentheses are balanced"""
    stack = Stack()
    balanced = True
    i = 0
    while i < len(line) and balanced:
        symbol = line[i]
        if symbol in ["(", "{", "[", "<"]:
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()
        i += 1
    return balanced and stack.is_empty()


def par_checker_file(filename):
    """Check expressions in the file"""
    input_file = open(filename, "r")
    line = input_file.readline().strip()
    while line != "":
        if par_checker(line):
            output = line + " is balanced"
            print(output)
        elif not par_checker(line):
            output = line + " is NOT balanced"
            print(output)
        line = input_file.readline().strip()
    input_file.close()


def base_converter(dec_num, base):
    """Convert a decimal number to any base"""

    # if base in [2, 8, 16]
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while dec_num > 0:
        rem = dec_num % base
        remstack.push(rem)
        dec_num = dec_num // base

    new_string = ""
    while not remstack.is_empty():
        new_string = new_string + digits[remstack.pop()]

    return new_string


def rpn_calc(postfix_expr):
    """Evaluate a postfix expression"""
    exp_stack = Stack()
    charlist = postfix_expr.split()

    # Evaluate expression using a stack
    for char in charlist:
        print(char)
        if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            exp_stack.push(int(char))
        elif char in ["+", "-", "*", "/"]:
            operator = char
            try:
                operand2 = exp_stack.pop()
                operand1 = exp_stack.pop()
            except IndexError:
                raise StackError("Stack is empty")
            answer = do_math(operator, operand1, operand2)
            exp_stack.push(answer)
        else:
            raise TokenError(f"Unknown token: {char}")

    # Return the answer (last thing in stack)
    try:
        if exp_stack.size() == 1:
            return exp_stack.pop()
        else:
            raise StackError("Stack is not empty")
    except IndexError:
        raise StackError("Stack is empty")


# Use with rpn_calc()
def do_math(op, op1, op2):
    """Evaluate a mathematical operation"""
    if op == "*":
        answer = op1 * op2
    elif op == "/":
        answer = op1 / op2
    elif op == "+":
        answer = op1 + op2
    elif op == "-":
        answer = op1 - op2
    return answer
