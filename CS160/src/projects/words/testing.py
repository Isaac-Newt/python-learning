class Stack:
    '''Implementing Stack ADT as a list'''
    def __init__(self):
        '''Initialize an instance'''
        self.items = []
    def is_empty(self):
        '''Is stack empty?'''
        return self.items == []
    def size(self):
        '''Return stack size'''
        return len(self.items)
    def push(self, item):
        '''Add new item to stack'''
        self.items.append(item)
    def pop(self):
        '''Remove an item from stack'''
        return self.items.pop()
    def peek(self):
        '''Look at the top item'''
        return self.items[-1]
    def clone(self):
        '''Cloning a stack'''
        # Create new stack
        cloned_stack = Stack()
        # copy self.items from one stack to the next
        for item in self.items:
            cloned_stack.push(item)
        # Return new stack
        return cloned_stack

stack_1 = Stack()
stack_1.push(1)
stack_1.push(2)
stack_1.push(3)

stack_2 = stack_1.clone()

print("Stack 1 size: ", stack_1.size()) # 3
print("Stack 2 size: ", stack_2.size()) # 3

print("Stack 1 top item: ", stack_1.peek()) # 3
print("Stack 2 top item: ", stack_2.peek()) # 3

stack_1.pop()

print("- - - - -")

print("Stack 1 size: ", stack_1.size()) # 2
print("Stack 2 size: ", stack_2.size()) # 3

print("Stack 1 top item: ", stack_1.peek()) # 2
print("Stack 2 top item: ", stack_2.peek()) # 3
