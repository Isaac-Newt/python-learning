def gcd(a_num: int, b_num: int) -> int:
    """
    Recursive GCD finder

    Using Euclid's Algorithm
    - gcd of a & b = gcd of b & a%b
    - gcd of a & 0 = a
    """
    if b_num == 0:
        print(a_num)
        return
    
    rem = (a_num % b_num)
    gcd(b_num, rem)

gcd(10, 25) #5
gcd(10, 3) #1
gcd(11, 13) #1
gcd(11, 121) #11
gcd(6, 27) #3