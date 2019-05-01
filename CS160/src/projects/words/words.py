'''
Isaac List - CS160 
April 28, 2019

Build a ladder of words using stacks and queues
'''
#!/usr/bin/env python3

WORDS_OF_3 = set()
WORDS_OF_4 = set()
WORDS_OF_5 = set()


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
        cloned_stack = Stack()
        for item in self.items:
            cloned_stack.push(item)
        return cloned_stack


class Queue:
    '''Implementing Queue ADT as a list'''
    def __init__(self):
        '''Initialize an instance'''
        self.items = []
    def is_empty(self):
        '''is the Queue empty'''
        return self.items == []
    def enqueue(self, item):
        '''Add an item'''
        self.items.insert(0, item)
    def dequeue(self):
        '''Remove an item'''
        return self.items.pop()
    def size(self):
        '''How big is it?'''
        return len(self.items)


def read_file(filename: str) -> dict:
    '''Read a file into 3 sets'''
    # Open File in read mode
    input_file = open(filename, "r")
    # Read the lines, sort into proper sets
    line = input_file.readline().strip()
    while line != "":
        if len(line) == 3:
            WORDS_OF_3.add(line)
        elif len(line) == 4:
            WORDS_OF_4.add(line)
        elif len(line) == 5:
            WORDS_OF_5.add(line)
        line = input_file.readline().strip()
    # Return a dictionary
    word_length_dictionary = {3: WORDS_OF_3, 4: WORDS_OF_4, 5: WORDS_OF_5}
    return word_length_dictionary


def distance(word1: str, word2: str) -> int:
    '''Differences between words'''
    distance = 0
    for idx in range(len(word1)):
        if word1[idx] != word2[idx]:
            distance += 1
    return distance


def diff_by_one_all(word, all_words, used_words):
    '''Find all words that differ by 1 letter'''
    candidates = []
    for candidate in all_words:
        if candidate not in used_words and distance(word, candidate) == 1:
            candidates.append(candidate)
    return candidates


def main():
    '''Main function'''
    read_file('data/projects/words/words.txt')

    word_start = 'stone'
    word_stop = 'water'
    found = False
    if len(word_start) != len(word_stop):
        raise Exception('You have to use words of the same length (3, 4, or 5 letters)')
    if (len(word_start)) == 3:
        words_to_use = WORDS_OF_3
    elif (len(word_start)) == 4:
        words_to_use = WORDS_OF_4
    elif (len(word_start)) == 5:
        words_to_use = WORDS_OF_5
    else:
        raise Exception('You have to use words of the same length (3, 4, or 5 letters)')
    
    print("Let's turn '%s' into '%s'" % (word_start, word_stop))

    # Create a Queue, each node will be a stack
    ladder_queue = Queue()

    # Create the stacks, and add to the queue
    words_used = []
    list_of_close_words = diff_by_one_all(word_start, words_to_use, words_used)

    for close_word in list_of_close_words:
        # Build stack with starting word and next step
        new_stack = Stack()
        new_stack.push(word_start)
        new_stack.push(close_word)
        # Add close word to the list of used words
        words_used.append(close_word)
        # Add the stack to the queue
        ladder_queue.enqueue(new_stack)
    # For each stack, find 1-away words of top item, 
    # clone and add close words, then append the bigger stack.
    #
    # If the target word is added, then set found to True
    while not found and len(words_used) < len(words_to_use):
        current_ladder = ladder_queue.dequeue()
        # Find 1-away words of top word
        top_word = current_ladder.peek()
        close_words = diff_by_one_all(top_word, words_to_use, words_used)
        # Clone stack, add word, and enqueue the new stack
        count = 0
        while count < len(close_words) and not found:
            if close_words[count] == word_stop:
                found = True
            new_clone_stack = current_ladder.clone()
            new_clone_stack.push(close_words[count])
            # Add close word to the list of used words
            words_used.append(close_words[count])
            # If found, then print the stack, otherwise continue
            if found:
               # print the stack
               stack_to_print = new_clone_stack
               print(stack_to_print.items)
            else:
                # Add the stack to the queue
                ladder_queue.enqueue(new_clone_stack)
                # print(ladder_queue.size())
            count += 1
    
    if found:
        print('Ladder found!')
        # print(stack_to_print)
        count = stack_to_print.size()
        list_of_words = []
        while count > 0:
            word = stack_to_print.pop()
            list_of_words.insert(0, word)
            count -= 1
        # print(list_of_words)
    else:
        print('Ladder not found')


if __name__ == '__main__':
    main()
