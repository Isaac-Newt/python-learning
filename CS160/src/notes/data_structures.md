# Data Structures

### Stacks, Queues, Dequeues, and Linked Lists

## Stacks - Things on top of other similar things

## Properties:

- A type of ADT (abstract data type)
- Can quantify size
- Cannot access just any element, must be from top of stack
- Can add to the top of the stack, not just anywhere you want

``` 
main() calls
    print() calls
        hello() calls
            write()
```
This forms a stack in the form:

|
---|
write |
hello |
print |
main |

# Linear Structures

- Include Stacks, queues
- Each element stays in the same position relative to its neighbors (those added prior and after)
- Have named ends:
    - Left/Rear/Top
    - Right/Front/Bottom
    - (In class: Stacks = Top/Bottom, Queues = Front/Rear)
    - Linked Lists are kinda more wobbly :o)
- Characteristics:
    - Stacks: Last element in is the first to go out, first in is last out
    - Queue: Last in is last out, first in is first out (except priorities, don't consider for now)
    - Double-Ended Queue (Dequeue): Can add and remove from both ends

# Operation and Implementation

## Stacks
- Create empty stack:
    - ```stack()```
- Add element: 
    - ```stack.push()```
    - Generally append to end of "list", return nothing
- Remove element: 
    - ```stack.pop()``` 
    - Pop from end of the "list", return the element popped
- Look at top element: 
    - ```stack.peek()``` 
    - Should return the last value in the "list"
- Check if empty (True or False): 
    - ```stack.is_empty()```
- Get the length/size: 
    - ```stack.size()```

### Implementing stack with lists in python:
```Python
class stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
```

### Implementing stack as a dictionary:

```Python
class Stack:
    def __init__(self):
        self.items = {}
        self.top = 0
    def is_empty(self):
        return self.items == {}
    def size(self):
        return len(self.items)
    def push(self):
        return 
    def pop(self):
        return 
    def peek(self):
        return 
```

### Stack applications:
- Parentheses checker
- Expression checker
- Function calls
- Grammar checker

# Infix, Prefix, Postfix

1 + 2 * 3 = 7

or 

1 + 2 * 3 = 9

### Infix: 1 + 2 * 3

### Prefix: + 1 * 2 3

### Postfix: 1 2 3 * + 

## Implement Postfix notation with a stack: --> chapter 3 in textbook

### Expression: 1 2 3 * + =
("=" indicates the end of the expression)

1 --> go to stack
- Stack = [1]

2 --> go to stack
- Stack = [1, 2]

3 --> go to stack
- Stack = [1, 2, 3]

\* --> pop 2 elements and multiply them, put result back on stack
- Stack = [1, 6]

\+ --> Pop 2 elements and add them, put result back on the stack
- Stack = [7]

Answer is the only element in the stack
- If more than one element in stack, expression was invalid