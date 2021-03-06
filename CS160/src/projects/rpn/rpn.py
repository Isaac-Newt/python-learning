#!/usr/bin/env python3
"""
Reverse Polish Notation

Isaac List - CS160
March 7, 2019
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
    """Evaluate postfix expression"""
    exp_stack = Stack()
    charlist = postfix_expr.split()
    # Evaluate expression using a stack
    for char in charlist:
        if char.isnumeric():
            exp_stack.push(int(char))
        elif char in ["+", "-", "*", "/", "%", "**", "//"]:
            operator = char
            try:
                operand2 = exp_stack.pop()
                operand1 = exp_stack.pop()
            except:
                raise StackError("Stack is empty")
            answer = do_math(operator, operand1, operand2)
            exp_stack.push(answer)
        elif char == "=":
            pass
        else:
            raise TokenError(f"Unknown token: {char}")

    # Return the answer (last thing in stack)
    try:
        if exp_stack.size() == 1:
            return exp_stack.pop()
        elif exp_stack.size() > 1:
            raise StackError("Stack is not empty")
        else:
            raise StackError("Stack is empty")
    except IndexError:
        raise StackError("Stack is empty")


def do_math(op: str, op1: int, op2: int) -> int:
    """process arithmetic operations"""
    if op in ["+", "-", "*", "/", "%", "**", "//"] and isinstance(op1 + op2, int):
        if op == "+":
            answer = op1 + op2
        elif op == "-":
            answer = op1 - op2
        elif op == "*":
            answer = op1 * op2
        elif op == "/":
            answer = op1 / op2
        elif op == "%":
            answer = op1 % op2
        elif op == "**":
            answer = op1 ** op2
        elif op == "//":
            answer = op1 // op2
    else:
        raise SyntaxError("invalid syntax")
    return answer


def rpn_calc(filename: str) -> int:
    """Read lines from the file and pass them to the postfix_eval"""
    input_file = open(filename, "r")
    line = input_file.readline().strip()
    checksum = 0
    while line != "":
        try:
            checksum += postfix_eval(line)
        except:
            print("Invalid Expression")
        line = input_file.readline().strip()
        print(checksum)
    input_file.close()
    return checksum


def main():
    """Main function"""
    checksum = rpn_calc("data/projects/rpn/rpn_input_1.txt")
    print(f"Checksum is {checksum:.2f}")


if __name__ == "__main__":
    main()
