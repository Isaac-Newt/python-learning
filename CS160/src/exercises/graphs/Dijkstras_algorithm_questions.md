## Isaac List - CS160 - May 3, 2019

## Dijkstra's Algorithm Questions

### Question 1: Find paths from node "t"

Step | t | u   | v     | w         | x         | y      | z 
  ---|---|---  |---    |---        |---        |---     |---
  0  | 0 | inf | inf   | inf       | inf       | inf    | inf
  1  | 0 | 2   | 4     | inf       | inf       | 7      | inf
  2  | 0 | 2   | 4 < 5 | (3+2) = 5 | inf       | 7      | inf
  3  | 0 | 2   | 4     | 5 < 8     | (3+4) = 7 | 7 < 12 | inf
  4  | 0 | 2   | 4     | 5         | 7 < 13    | 7      | (7+12) = 19
  5  | 0 | 2   | 4     | 5         | 7         | 7 < 11 | 19
  6  | 0 | 2   | 4     | 5         | 7         | 7      | 19 > 15
  7  | 0 | 2   | 4     | 5         | 7         | 7      | 15

### Question 2: Find paths from node "x"

Step | t         | u         | v      | w     | x | y      | z 
  ---|---        |---        |---     |---    |---|---     |---
  0  | inf       | inf       | inf    | inf   | 0 | inf    | inf
  1  | inf       | inf       | 3      | 6     | 0 | 6      | 8
  2  | (3+4) = 7 | (3+3) = 6 | 3      | 6 < 7 | 0 | 6      | 8 < 23
  3  | 7         | 6 < 9     | 3 < 10 | 6     | 0 | 6 < 11 | 8
  4  | 7 < 13    | 6         | 3 < 14 | 6     | 0 | 6      | 8 < 18
  5  | 7         | 6         | 3      | 6     | 0 | 6 < 20 | 8
  6  | 7 < 11    | 6         | 3 < 12 | 6     | 0 | 6      | 8
  7  | 7         | 6         | 3      | 6     | 0 | 6      | 8