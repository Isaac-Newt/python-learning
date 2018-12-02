# Isaac List - November 2, 2018 - Lab 9 Part 5


def runningSum(numbers) :
    sum = 0
    runningTotalList = []
    
    # You can do for loops over lists! :)
    for number in numbers:
        sum += number
        runningTotalList.append(sum)
        
    return runningTotalList


print(runningSum([ ]))
print(runningSum([ 100 ]))
print(runningSum([ 100, 200, 300 ]))
print(runningSum([ 300, 0, 200, -100, 999, 100, -200, -300 ]))
