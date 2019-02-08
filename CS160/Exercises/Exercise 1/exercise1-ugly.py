def findFirstNonRepeat(string):
    dictionaryOfCharacters = {}
    for int in range(len(string)):
        if string[int] in dictionaryOfCharacters:
            dictionaryOfCharacters[string[int]] += 1
        else:
            dictionaryOfCharacters[string[int]] = 1
    count, found, answer = 0, False, ""
    while count < len(string) and found == False:
        key = string[count]
        if dictionaryOfCharacters[key] == 1:
            answer = key
            found = True
        count += 1
    return answer
string = input("Enter a string: ")
print("The first non-repeated character is:", findFirstNonRepeat(string))