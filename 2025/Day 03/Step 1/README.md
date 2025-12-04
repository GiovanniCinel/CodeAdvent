# Day 3: Lobby

## Problem Overview
The elevators are offline, and you need to power an emergency escalator using banks of batteries found in the lobby. You must calculate the maximum power output ("Joltage") achievable from each bank.

## Battery Rules
- Input consists of lines of digits (e.g., `987654321`).
- Each line represents one **Battery Bank**.
- Each digit represents a battery's potential rating (`1` to `9`).

### Power Generation Mechanics
1. **Select exactly two batteries** from the bank.
2. **Preserve their order:** You cannot rearrange the batteries physically. The first selected battery must appear to the *left* of the second selected battery in the original string.
3. **Form the Joltage:** Concatenate the two digits to form a 2-digit number.
   - *Example:* Bank `12345`. Select `2` and `4`. Result: `24` Joltage.
   - *Invalid:* You cannot select `4` then `2` to make `42`, because `4` appears after `2` in the bank.

## Goal
For each bank (line), find the combination of two batteries that produces the **highest possible Joltage number**, then sum these maximums together.

## Example Scenarios

### Detailed Analysis
**Bank 1:** `987654321111111`
- Best strategy: Pick the first `9`, then the `8` immediately following it.
- Result: **98**

**Bank 2:** `811111111111119`
- Best strategy: Pick the `8` (start), then the `9` (end).
- Result: **89**

**Bank 3:** `234234234234278`
- Analysis: High numbers are at the end.
- Best strategy: Pick `7`, then `8`.
- Result: **78**

**Bank 4:** `818181911112111`
- Analysis: There is a `9` in the middle.
- We pick `9` as the first digit. We need the highest number appearing *after* it.
- The highest digit after `9` is `2`.
- Result: **92**

### Calculation
- Sum of maximums: `98 + 89 + 78 + 92`
- **Total Output:** `357`

## Challenge
Process your puzzle input to determine the maximum joltage for every bank and calculate the grand total.

## Input
- Multiple lines of text, each containing a string of digits.

## Output
- A single integer representing the sum of all maximum joltages.