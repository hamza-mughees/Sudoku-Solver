# Sudoku Solver

This project uses a back-tracking algorithm to solve the Sudoku puzzle. It prints out all the possible solutions for a given puzzle.

**Input**

The input is a file with a Sudoku puzzle, in the form of integers between 1 and 9 inclusive, separated by spaces, like so:

```
9 0 6 0 7 0 4 0 3
0 0 0 4 0 0 2 0 0
0 7 0 0 2 3 0 1 0
5 0 0 0 0 0 1 0 0
0 4 0 2 0 8 0 6 0
0 0 3 0 0 0 0 0 5
0 3 0 7 0 0 0 5 0
0 0 7 0 0 5 0 0 0
4 0 5 0 1 0 7 0 8
```

**Output**

The code solves the input Sudoku puzzle and outputs all possible solutions, as follows:

```
Solution 1
[9, 2, 6, 5, 7, 1, 4, 8, 3]
[3, 5, 1, 4, 8, 6, 2, 7, 9]
[8, 7, 4, 9, 2, 3, 5, 1, 6]
[5, 8, 2, 3, 6, 7, 1, 9, 4]
[1, 4, 9, 2, 5, 8, 3, 6, 7]
[7, 6, 3, 1, 4, 9, 8, 2, 5]
[2, 3, 8, 7, 9, 4, 6, 5, 1]
[6, 1, 7, 8, 3, 5, 9, 4, 2]
[4, 9, 5, 6, 1, 2, 7, 3, 8]

Solution 2
[9, 2, 6, 5, 7, 1, 4, 8, 3]
[3, 5, 1, 4, 8, 6, 2, 7, 9]
[8, 7, 4, 9, 2, 3, 5, 1, 6]
[5, 8, 2, 3, 6, 7, 1, 9, 4]
[1, 4, 9, 2, 5, 8, 3, 6, 7]
[7, 6, 3, 1, 9, 4, 8, 2, 5]
[2, 3, 8, 7, 4, 9, 6, 5, 1]
[6, 1, 7, 8, 3, 5, 9, 4, 2]
[4, 9, 5, 6, 1, 2, 7, 3, 8]
```
