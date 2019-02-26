# Algorithm Efficiency

## Compare digits to multiply and calculation time

digits | time (s) | example
---|---|---
1 | 1 | 4 x 7
2 | 10 | 41 x 57
3 | x | 103 x 324
4 | x | 5367 x 5097
5 | x | 10653 x 33264

# Big-O Notation

- Is n + 1 faster than n + 5? Yes, doesn't matter if n is big.

- Is 2n + 1 faster than 3n + 1? Yes, doesn't matter if n is big.

- Is 2n^2 + 3n + 5 faster than n^3? Yes, because it grows more slowly.

i.e. "faster" refers to a function that grows more slowly as n --> infinity

### O(2n^2 + 3n + 5) = O(n^2)

- Only look at the magnitude of the highest power

## Sometimes size is not the only factor in efficiency
- Evaluate best case, worst case, and average case
- Performance can suffer in specific cases, important to know this in advance of use.

## Functions in order of growth rate

(i.e. slower as you go down the list, best to worst)

f(n) | Name
---|---
1 | Constant
log(n) | Logarithmic
n | Linear
n*log(n) | Log Linear
n^2 | Quadratic
n^3 | Cubic
2^n | Exponential
n! | Factorial (Brute-Force)

---

## Anagram decoder
Algorithm and Logarithm
- Brute Force 
    - (find all possible anagrams of one word, compare to the other) --> O(n!)
- Checking off letters 
    - (for each letter in word 2, search through word 1) --> O(n^2)
- Sort alphabetically and compare 
    - (should be same) 
    - O(n^2) or O(nlog(n)) depending on sorting algorithm
- Count instances of letters and compare
    -  --> O(n)

# Look these up!

## Python list performance

Operation | Big-O Efficiency
---|---
index[] | O(1)
append | O(1)
pop() | O(1)
pop(i) | O(n)
insert(i, item) | O(n)
iteration | 
in | 
reverse | 
concatenate | 
sort | 

## Python Dictionary Efficiency
Operation | Big-O Efficiency
---|---
copy | 
