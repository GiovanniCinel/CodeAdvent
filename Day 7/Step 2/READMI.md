
# Day 7: Bridge Repair - Part Two

## Problem Overview

The engineers are still struggling to repair the bridge. After reviewing your calculations, they discover a third operator that had been overlooked: **concatenation (`||`)**. This operator allows two numbers to be joined into a single number by combining their digits.

Using this newfound operator, additional calibration equations can now be validated. Your task is to re-evaluate the equations and determine the total calibration result.

---

## Task Description

### Problem Details

1. **Operators**  
   - **Addition (`+`)**: Adds two numbers.  
   - **Multiplication (`*`)**: Multiplies two numbers.  
   - **Concatenation (`||`)**: Combines two numbers by joining their digits.  
     Example: `12 || 345 = 12345`.

2. **Evaluation Rules**  
   - Operators are evaluated **left-to-right** (no precedence rules).  
   - Numbers must remain in their given order; they cannot be rearranged.

3. **Objective**  
   - Identify all valid equations, considering all three operators.  
   - Compute the **total calibration result** by summing the test values of the valid equations.

---

### Example Walkthrough

**Input:**  
```
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
```

**Output:**  
The valid equations are:
- **190:** `10 * 19`
- **3267:** `81 + 40 * 27` and `81 * 40 + 27`
- **292:** `11 + 6 * 16 + 20`
- **156:** `15 || 6`
- **7290:** `6 * 8 || 6 * 15`
- **192:** `17 || 8 + 14`

The total calibration result is:  
`190 + 3267 + 292 + 156 + 7290 + 192 = 11387`.

---

## Solution Requirements

1. **Determine Valid Equations:**  
   - For each equation, generate all possible combinations of operators.
   - Evaluate each combination left-to-right.
   - Check if the result matches the test value.

2. **Compute Total Calibration Result:**  
   - Sum the test values of all valid equations.

---

## Input Format

A list of equations where:
- Each line contains a test value (integer) followed by a colon and space-separated numbers.

Example:  
```
190: 10 19
3267: 81 40 27
156: 15 6
```

---

## Output Format

A single integer representing the total calibration result of all valid equations.