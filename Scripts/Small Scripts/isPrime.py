def is_prime(n):
    decision = False
    if n < 2:
        decision = False
    else:
        for int in range(2, n-1):
            if n % int != 0:
                decision = True
    return decision

# True
print(is_prime(2))
print(is_prime(4813))

# False
print(is_prime(22))
print(is_prime(4187))