# Calculator using basic operators, but like, manually

# This thing really doesn't work at this point, just doing it
# for some fun exercises.  Use at your own risk :)

# check to see if is operator
def isOperator(x):
    if x == "+" or x == "-" or x == "*" or x == "/" x == "%":
        return True
    else:
        return False

# Return the relevant operator
def findOperator(list, index):
    o = list[index]
    if o == "+" or o == "-" or o == "/" or o == "%":
        return o
    elif o == "*":
        if list[index + 1] == "*":
            return "**"
        else:
            return "*"

# Check to see if is number
def isNumberPart(x):
    if x == "0" or x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9" or x == ".":
        return True

# build a string of each number
def buildNumber(char):
    number = str(exp[char])
    if isNumberPart(exp[char + 1]):
        buildNumber(exp[char + 1])
    else:
        return float(number)

# evaluation function
def evaluate(exp):
    result = ""

    expression = []

    # Ignore spaces
    elif exp[char] == " ":
            pass

    # Operator
    if isOperator(exp[char]):
        operator = findOperator(exp, exp[char])
        expression.append(operator)

    # Number
    elif isNumberPart(exp[char]):
        number = buildNumber(exp[char])
        expression.append(number)

    return result

# Get a string of numbers and operators
expression = input("Enter an expression:" )

result = evaluate(expression)

print(result)
