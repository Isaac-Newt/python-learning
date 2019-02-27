#!/usr/bin/env python3
"""
Touchscreen Keyboard

Isaac List - CS160
February 26, 2019
"""

# Beautiful Dictionary Heaven :)
top = {"q": 0, "w": 1, "e": 2, "r": 3, "t": 4, "y": 5, "u": 6, "i": 7, "o": 8, "p": 9}
    
mid = {"a": 0, "s": 1, "d": 2, "f": 3, "g": 4, "h": 5, "j": 6, "k": 7, "l": 8}

low = {"z": 0, "x": 1, "c": 2, "v": 3, "b": 4, "n": 5, "m": 6}

def find_distance(char_1: str, char_2: str):
    distance = 0
    # If they are in the same row
    if ((char_1 in top) and (char_2 in top)):
        distance = abs(top[char_1] - top[char_2])
    if ((char_1 in mid) and (char_2 in mid)):
        distance = abs(mid[char_1] - mid[char_2])
    if ((char_1 in low) and (char_2 in low)):
        distance = abs(low[char_1] - low[char_2])

    # If one is in top and one is in mid
    if ((char_1 in top) and (char_2 in mid)):
        distance = abs(top[char_1] - mid[char_2]) + 1
    if ((char_1 in mid) and (char_2 in top)):
        distance = abs(mid[char_1] - top[char_2]) + 1

    # If one is in top and one is in low
    if ((char_1 in top) and (char_2 in low)):
        distance = abs(top[char_1] - low[char_2]) + 2
    if ((char_1 in low) and (char_2 in top)):
        distance = abs(low[char_1] - top[char_2]) + 2

    # If one is in mid and one is in low
    if ((char_1 in mid) and (char_2 in low)):
        distance = abs(mid[char_1] - low[char_2]) + 1
    if ((char_1 in low) and (char_2 in mid)):
        distance = abs(low[char_1] - mid[char_2]) + 1

    return distance

def spell_check(filename: str) -> None:
    """Rank words by their proximity to the target"""
    # Open the file in read mode
    file = open(filename, "r")

    # Read first line --> number of test cases
    number_of_test_cases = int(file.readline())

    # For each test case ... 
    for idx in range(number_of_test_cases):
        # dictionary of suggestions and their distances from the typed word
        suggestion_distances = []

        # Read the first line of this test case
        first_test_line = file.readline().strip().split()

        # Gives number of "suggestions", the second item in the split list thing
        lines_in_test = int(first_test_line[1])
        # For testing only!
        # print("Lines in test: ", lines_in_test)

        # Find word that was "typed", this is the first item in the split list
        word_typed = first_test_line[0]
        # For testing only!
        # print("This is the word: ", word_typed)

        # Go through each suggestion and find distance to second_line
        for line in range(lines_in_test):
            # The suggestion includes a "\n" terminator, so exclude that
            suggestion = file.readline().strip()

            # Word distance starts at 0, add to it based on each letter's distance
            word_distance = 0
            for idx in range(len(suggestion)):
                word_distance += find_distance(word_typed[idx], suggestion[idx])
            suggestion_distances.append((word_distance, suggestion))

        # Sort the dictionary by the values, low to high
        for item in sorted(suggestion_distances):
            print(item[1], item[0])

        # write to file, but later.  For now, just print to console
        # for item in suggestion_distances:
        #     print(f"{item}")

def main():
    """Entry point"""
    spell_check("data/projects/keyboard/sample.in")


if __name__ == "__main__":
    main()
