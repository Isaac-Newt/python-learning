class Node:
    def __init__(self, init_value):
        self._value = init_value
        self._next = None

    def get_data(self):
        return self._value

    def set_data(self, new_data):
        self._value = new_data

    data = property(get_data, set_data)

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next):
        self._next = new_next

    def __str__(self):
        return str(self._value)


class LinkedList:
    def __init__(self):
        self._head = None
        # self._tail = None
        self._size = 0

    # Call with len(list_obj)
    def __len__(self) -> int:
        return self._size

    # Print in format: "[obj1, obj2, obj3]"
    # This simply a style choice, not committed standard
    def __str__(self) -> str:
        list_str = "["
        current = self._head
        # This is one way to build the string
        while current:
            list_str += str(current)
            if current.next:
                list_str += ", "
            current = current.next
        list_str += "]"
        return list_str

        # An equivilant way to build string
        my_list = []
        current = self._head
        while current:
            my_list.append(current.data)
            current = current.next
        return f[{", ".join(my_list)}]

    def is_empty(self) -> bool:
        # Check the head
        return self._head is None
        # Or check the size
        return self.size == 0

    def size(self) -> int:
        return self._size

    # This adds a new node to the top of the list
    # Point new_node.next to whatever head is pointing to,
    # and then move head to point to new_node
    def add(self, new_node: object) -> None:
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def search(self, value) -> bool:
        current = self._head
        while current:  # not None
            # If data found, return true.  Otherwise, return False
            if current.data == value:
                return True
            current = current.next  # Will eventually become None
        return False

    # List has no real concept of index, so use index as a counter
    # for a loop, and if/when desired value found, return the "idx"
    # If not found, return index of "-1" (convention standard)
    def index(self, value) -> int:
        """
        Return the index of an element in the list

        Useful method
        """
        idx = -1  # Use imaginary index as counter
        current = self._head
        while current:
            if current.data == value:
                return idx
            current = current.next
            idx += 1
        # This is a convention to denote that an item was not found
        return -1

    # Add new_node as the final link in the list
    #
    # This expects a node object, so should be called as:
    #   llobject.append(Node(item))
    # Could make the choice to create a node within the fn:
    #   llobject.append(item)
    # Just need to be self-consistent
    def append(self, new_node: object) -> None:  # Expect object (Node)
        # Example of a well-written docstring
        """
        Append a new Node to the list

        Takes Node object as a parameter
        """
        # If the list is empty
        # Necessary, because if we start with current as what head
        # points to, and it does not exist, we cannot check to see
        # if current.next exists, since, current does not exist
        if not self._head:
            self._head = new_node
            self._size += 1
            return
        # While current.next exists, keep moving.  Once it doesn't
        # exist, point current.next to new_node
        current = self._head
        while current.next:
            current = current.next
        current.next = new_node
        self._size += 1

    def insert(self, pos: int, new_node: object) -> None:
        current = self._head
        idx = 0
        # If position is <= 0, gets added to front like normal "add"
        if pos <= 0:
            self.add(new_node)
            return
        # If position is bigger than the list, append the node
        if pos > self._size:
            self.append(new_node)
            return
        # What to actually do for fun stuff :)
        # use "idx" from the top of the function
        while idx < pos - 1:
            idx += 1
            current = current.next
        # 
        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def pop(self, idx = None):
        if not self._head:
            raise Exception("Cannot pop from an empty list")
        if idx == None:
            idx = self._size
        if idx < 0:
            raise ValueError("Negative")
        current = self._head
        prev = None
        cur_idx = 0
        while current.next and cur_idx < idx:
            prev = current
            current = current.next
            cur_idx += 1
        result = current.data
        if prev:
            prev.next = current.next
        else:
            self._head = current.next
        self._size -= 1
        return result


def main():
    # print('Working with nodes')
    # n = Node('A')
    # print(n.data)
    # print(n.next)
    # print(n)

    # m = Node('B')
    # n.next = m
    # print(n.next)

    print("Working with lists")
    ll = LinkedList()
    # print(ll.size())  # 0
    # print(type(ll))  # LinkedList
    # print('Printing a list')
    # print(ll)
    # ll.add(Node('Q'))
    # print(ll)  # [Q]
    # ll.add(Node('A'))
    # print(ll)  # [A, Q]
    # ll.add(Node('D'))
    # print(ll)  # [D, A, Q]
    # print(len(ll))
    # print(ll.search('Z'))
    # print(ll)  # [D, A, Q]
    # print(len(ll))
    # print(ll.index('D'))  # 0
    # print(ll)  # [D, A, Q]
    # print(len(ll))
    # print(ll.index('Z'))  # -1
    # print(ll)  # [D, A, Q]
    # print(len(ll))
    # print('Inserting a new node')
    # ll.insert(0, Node('K'))
    # print(ll)  # [K, D, A, Q]
    # print(len(ll))  # 4
    # ll.insert(2, Node('M'))
    # print(ll)  # [K, D, M, A, Q]
    # print(len(ll))  # 5
    print(ll)  # []
    ll.append(Node("R"))
    ll.append(Node("Q"))
    ll.append(Node("T"))
    ll.append(Node("S"))
    print(ll)  # [R, Q, T, S]
    print(len(ll))  # 4
    print(ll.pop(1))  # Q
    print(ll)  # [R, T, S]
    print(len(ll))  # 3
    print(ll.pop())  # S
    print(ll)  # [R, T]
    print(len(ll))  # 2
    print("---")
    print(ll.pop(0))  # R
    print(ll)  # [T]
    print(len(ll))  # 1


if __name__ == "__main__":
    main()
