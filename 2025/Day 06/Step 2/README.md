# Day 6: Trash Compactor - Part Two

## Problem Overview
The cephalopods point out a critical misunderstanding: their math is read **Right-to-Left**, and numbers are constructed vertically within columns, not horizontally.

## New Parsing Rules

### 1. Identify Vertical Numbers
- Instead of reading rows (`123`), look at vertical columns.
- **Top Digit:** Most Significant Digit (Thousands/Hundreds...).
- **Bottom Digit:** Least Significant Digit (Ones).
- **Empty Spaces:** Ignore them; they don't count as digits.

### 2. Processing Order (Right-to-Left)
- Within a single problem block, read the columns starting from the **Right** and moving to the **Left**.
- The mathematical operation is applied in that order.

### 3. Operator
- The operator (`+` or `*`) is still located at the bottom of the block.
- It applies to all numbers found in that block.

## Example Analysis
*Using the leftmost problem from the example grid:*

**Raw Block:**
```
123 
 45 
  6 
*
```

**Step 1: Parse Columns (Left to Right indices)**
- **Col 1:** Top:`1`, Mid:` ` , Bot:` ` -> Number: **1**
- **Col 2:** Top:`2`, Mid:`4`, Bot:` ` -> Number: **24**
- **Col 3:** Top:`3`, Mid:`5`, Bot:`6` -> Number: **356**

**Step 2: Apply Right-to-Left Order**
- 1st Number: **356** (from Col 3)
- 2nd Number: **24** (from Col 2)
- 3rd Number: **1** (from Col 1)

**Step 3: Calculate**
- Equation: `356 * 24 * 1`
- Result: **8544**

*(Contrast this with Part 1, where we read `123 * 45 * 6 = 33210`)*

## Summary of Changes
| Feature | Part One | Part Two |
| :--- | :--- | :--- |
| **Number Orientation** | Horizontal Rows | Vertical Columns |
| **Digit Order** | Left(MSD) -> Right(LSD) | Top(MSD) -> Bottom(LSD) |
| **Problem Reading** | Top -> Bottom | Right -> Left |

## Challenge
Re-parse the entire worksheet using the Cephalopod Right-to-Left vertical logic. Calculate the new grand total.

## Input
- The same worksheet text as Part One.

## Output
- A single integer representing the new grand total sum.