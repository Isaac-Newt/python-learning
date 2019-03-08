# .isnumeric()

#!/usr/bin/env python3
"""
Reverse Polish Notation

Isaac List - CS160

March 6, 2019
"""

from pythonds3.basic import Stack


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


class TokenError(Exception):
    """Token errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


def postfix_eval(postfix_expr: str) -> int:
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

def do_math(op: str, op1: int, op2: int) -> int:
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

def rpn_calc(filename: str) -> int:
    # TODO: Read lines from the file and pass them to the postfix_eval
    try:
        file = open(filename, "r")
    except:
        raise ValueError("File does not exist")
    while line != "":
        print(line)
        answer = postfix_eval(line)
        print(answer)
        

def main():
    """Main function"""
    checksum = rpn_calc("data/projects/rpn/rpn_input_1.txt")
    print(f"Checksum is {checksum:.2f}")


if __name__ == "__main__":
    main()
