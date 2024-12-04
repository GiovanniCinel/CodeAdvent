# Day 4: Ceres Search

## Problem Overview

The Historians have arrived at the Ceres monitoring station, and a small Elf there needs help with a word search. The goal is to find all instances of the word "XMAS" within the provided word search grid.

### Word Search Rules

- The word "XMAS" can appear horizontally, vertically, diagonally, backwards, or overlapping other words
- The task is to find all occurrences of "XMAS", not just one instance

### Example Walkthrough

Consider the following example word search:

```
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```

In this example, "XMAS" appears a total of 18 times.

Here's the same word search, with letters not involved in any "XMAS" replaced with `.`:

```
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
```

### Your Task

Take a look at the little Elf's word search and determine how many times the word "XMAS" appears.

## Input

- A grid of letters representing the word search

## Output

- The number of times the word "XMAS" appears in the word search
