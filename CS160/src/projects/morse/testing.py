input_file = open("data/projects/morse/morse.txt", "r")
for line in input_file:
    # Get the line
    line = line.strip()
    print(line)
    # Split into letter and code
    letter_code = line.split()
    letter = letter_code[0]
    code = letter_code[1]
    # Place the letter in its spot based on the code
    for char in code:
        if char == ".":
            print("left")
        elif char == "-":
            print("right")