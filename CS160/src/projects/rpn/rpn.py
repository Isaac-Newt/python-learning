#!/usr/bin/env python3
"""
Reverse Polish Notation
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
        print(char)
        try:
            if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                exp_stack.push(int(char))
            elif char in ["+", "-", "*", "/"]:
                operator = char
                try:
                    operand2 = exp_stack.pop()
                    operand1 = exp_stack.pop()
                except:
                    raise StackError
                answer = do_math(operator, operand1, operand2)
                exp_stack.push(answer)
        except:
            raise TokenError

    # Return the answer (last thing in stack)
    try:
        return exp_stack.pop()
    except:
        raise StackError


def do_math(op: str, op1: int, op2: int) -> int:
    # TODO: Process arithmetic operations
    if op == "+":
        answer = op1 + op2
    elif op == "-":
        answer = op1 - op2
    elif op == "*":
        answer = op1 * op2
    elif op == "/":
        answer = op1 / op2
    else:
        answer = op1 % op2
    return answer

def rpn_calc(filename: str) -> int:
    # TODO: Read lines from the file and pass them to the postfix_eval
    raise NotImplementedError


def main():
    """Main function"""
    checksum = rpn_calc("data/projects/rpn/rpn_input_1.txt")
    print(f"Checksum is {checksum:.2f}")


if __name__ == "__main__":
    main()
