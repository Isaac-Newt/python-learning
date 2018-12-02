# Isaac List - November 2, 2018 - Lab 9 Part 4

def sumListToFirstNegative(numbers) :

    sum = 0
    negativeHit = False
    index = 0
    
    while index < len(numbers) and not negativeHit:
        if numbers[index] < 0:
            negativeHit = True
        else:
            sum += numbers[index]
        
        index += 1
    
    return sum

print(sumListToFirstNegative([]))
print('====')
print(sumListToFirstNegative([100]))
print('====')
print(sumListToFirstNegative([100, 200, 300]))
print('====')
print(sumListToFirstNegative([300, 0, 200, -100, 999, 100, -200, -300]))
