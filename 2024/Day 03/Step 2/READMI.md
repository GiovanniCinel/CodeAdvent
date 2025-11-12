# Day 3: Mull It Over - Part Two

## Problem Continuation

As you scan the corrupted memory, you notice that there are also some conditional statements that need to be handled. These instructions can enable or disable the future "mul" instructions.

### New Instructions

1. `do()` instruction: Enables future `mul` instructions
2. `don't()` instruction: Disables future `mul` instructions

The most recent `do()` or `don't()` instruction applies. By default, `mul` instructions are enabled at the beginning of the program.

### Example Walkthrough

Consider the following corrupted memory:

```
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
```

In this example:
- `mul(2,4)` and `mul(3,7)` are enabled and valid
- `mul(5,5)` and `mul(11,8)` are disabled due to the `don't()` instruction
- `mul(8,5)` is re-enabled by the `undo()` instruction

The sum of the enabled multiplication results is 48 (2*4 + 8*5).

### Your Task

Handle the new `do()` and `don't()` instructions in the corrupted memory. Add up the results of only the enabled `mul` instructions.

## Input

- A string representing the corrupted memory with conditional statements

## Output

- An integer representing the sum of all the results from the enabled `mul` instructions