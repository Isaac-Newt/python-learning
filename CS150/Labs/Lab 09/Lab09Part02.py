# Isaac List - November 2, 2018 - Lab 9 Part 2

def sumList(numbers) :

    sum = 0
    for index in range(len(numbers)):
        sum = sum + numbers[index]
        
    return sum


print(sumList([]))
print('====')
print(sumList([100]))
print('====')
print(sumList([100, 200, 300]))
print('====')
print(sumList([300, 0, 200, -100, 999, 100, -200, -300]))
