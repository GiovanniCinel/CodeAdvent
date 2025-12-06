# Day 6: Trash Compactor

## Problem Overview
Trapped in a garbage smasher with a family of cephalopods, you must assist with their math homework to get the door opened. The worksheet presents math problems in a non-standard vertical layout.

## Worksheet Layout
- The input is a block of text containing numbers and operators.
- **Orientation:** Problems are arranged **vertically** in columns.
- **Separators:** Problems are separated by one or more columns of whitespace (spaces).
- **Structure per Problem:**
  - Top Rows: A series of numbers aligned vertically.
  - Bottom Row: An operator symbol (`+` or `*`).

## Calculation Rules
1. **Isolate Columns:** Identify distinct vertical groups of numbers separated by empty space.
2. **Identify Operation:** Look at the symbol at the very bottom of the group.
   - `+`: Sum all the numbers in that vertical group.
   - `*`: Multiply all the numbers in that vertical group.
3. **Grand Total:** Calculate the sum of all individual problem results.

## Example Scenario

### Input Grid
```
123 328 51 64 
 45 64 387 23 
  6 98 215 314
*   +  *   +
```

### Parsing & Solving

**Problem 1 (Column 1):**
- Numbers: `123`, `45`, `6`
- Operator: `*`
- Action: `123 * 45 * 6`
- Result: **33,210**

**Problem 2 (Column 2):**
- Numbers: `328`, `64`, `98`
- Operator: `+`
- Action: `328 + 64 + 98`
- Result: **490**

**Problem 3 (Column 3):**
- Numbers: `51`, `387`, `215`
- Operator: `*`
- Action: `51 * 387 * 215`
- Result: **4,243,455**

**Problem 4 (Column 4):**
- Numbers: `64`, `23`, `314`
- Operator: `+`
- Action: `64 + 23 + 314`
- Result: **401**

### Final Calculation
- Sum of results: `33210 + 490 + 4243455 + 401`
- **Grand Total:** `4,277,556`

## Challenge
Process the full worksheet (which is much wider than the example). Calculate the grand total of all vertical math problems.

## Input
- A block of text representing the worksheet.
- **Note:** The text may be very wide. Alignment of digits within a column may vary, but they are distinct from neighboring columns by empty space.

## Output
- A single integer representing the sum of all problem answers.