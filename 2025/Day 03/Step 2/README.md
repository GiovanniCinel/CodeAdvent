# Day 3: Lobby - Part Two

## Problem Overview
The escalator requires significantly more power to overcome static friction. The "Joltage Limit Safety Override" has been activated, allowing for a much larger selection of batteries.

## Updated Configuration
- **Objective:** Select **exactly 12** batteries from each bank.
- **Constraint:** Preserve the original relative order (left-to-right).
- **Goal:** Maximize the resulting 12-digit integer.

### The Selection Logic (Greedy Strategy)
To form the largest possible 12-digit number, you must prioritize the Most Significant Digit (the leftmost one).
1. **Digit 1:** Must be the largest number available in the bank, *provided* there are still at least 11 digits remaining to its right to complete the sequence.
2. **Digit 2:** Must be the largest number available to the right of Digit 1, *provided* there are still at least 10 digits remaining to its right.
3. **Repeat** until 12 digits are selected.

## Example Scenarios

### Comparative Analysis

**Bank 1:** `987654321111111`
- *Length:* 15 digits.
- *Strategy:* We need 12. We can only "skip" 3 digits total. Since the start is high (`987...`), we keep the start and drop the excess `1`s at the end.
- *Result:* `987654321111`

**Bank 3:** `234234234234278`
- *Strategy:* The number starts low (`2...`). We skip the initial `2` and `3` to grab a `4` as the starting digit.
- *Result:* `434234234278`

**Bank 4:** `818181911112111`
- *Strategy:* We want high digits early.
- We skip the `1`s between the `8`s.
- We grab `8`, `8`, `8`, `9`.
- Then fill the rest with the remaining digits to reach count 12.
- *Result:* `888911112111`

### Calculation
- Sum of large integers:
  `987654321111 + 811111111119 + 434234234278 + 888911112111`
- **Total Output:** `3121910778619`

## Challenge
Process the input banks again. Find the maximum possible 12-digit subsequence for each bank and calculate the sum of these massive numbers.

## Input
- Same list of battery banks (digit strings) as Part One.
- *Note:* All input strings must have a length of at least 12.

## Output
- A single (very large) integer representing the total output joltage.