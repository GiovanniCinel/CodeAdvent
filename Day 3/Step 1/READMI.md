# Day 3: Mull It Over

## Problem Overview

The North Pole Toboggan Rental Shop's computers are experiencing issues due to corrupted memory. Your task is to scan the corrupted memory and find the valid "mul" instructions to perform the necessary multiplications.

### Background

- The goal of the program is to multiply some numbers
- The instructions are in the form of "mul(X,Y)", where X and Y are 1-3 digit numbers
- However, the memory is corrupted, so there are also many invalid characters that should be ignored

### Puzzle Challenge

Scan the corrupted memory and find the valid "mul" instructions. Add up the results of all the valid multiplications.

### Example Walkthrough

Consider the following corrupted memory:

```
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
```

In this example, only the four highlighted sections are valid "mul" instructions:

1. `mul(2,4)` - Result: 8
2. `mul(3,7)` - Result: 21
3. `mul(32,64)` - Result: 2048
4. `mul(11,8)` - Result: 88
5. `mul(8,5)` - Result: 40

Adding up the results of these valid multiplications gives a total of 161.

### Your Task

Scan the corrupted memory provided as input and find all the valid "mul" instructions. Add up the results of all the valid multiplications.

## Input

- A string representing the corrupted memory

## Output

- An integer representing the sum of all the valid multiplication results