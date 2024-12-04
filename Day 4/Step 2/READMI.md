# Day 4: Ceres Search - Part Two

## Problem Continuation

It turns out the word search provided is not for "XMAS", but rather for "X-MAS". The goal is to find all occurrences of "X-MAS" within the grid, where "MAS" must be in the shape of an "X".

### X-MAS Criteria

- The "MAS" must be in the shape of an "X"
- The "MAS" can be written forwards or backwards within the "X" shape
- Irrelevant characters are represented by "."

### Example Walkthrough

Consider the following example word search:

```
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
```

In this example, an "X-MAS" appears 9 times.

### Your Task

Analyze the provided word search and determine how many times an "X-MAS" appears.

## Input

- A grid of letters representing the word search

## Output

- The number of times an "X-MAS" appears in the word search
