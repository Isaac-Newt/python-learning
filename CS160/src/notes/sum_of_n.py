def sum_of_n(n):
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + 1
    return the_sum

print(sum_of_n(50000000000))

# How do you determine the program's efficiency?

# Big-O estimate

# a = 5                   #1
# b = 6                   #1
# c = 10                  #1
# for i in range(n):      #3n^2
#     for j in range(n):
#         x = i*i
#         y = j*j
#         z = i*j
# for k in range(n):      #2n
#     w = a * k + 45
#     v = b * b
# d = 33                  #1

