print("Hello!")

print("What is your bill?")
sale = float(input())

print("What is your state?")
state = input()

if state == "WI":
    rate = 0.055
elif state == "MN":
    rate = 0.0688
elif state == "KY":
    rate = 0.06

tax = rate * sale

total = sale + tax

print("Your total is $" + str(total))