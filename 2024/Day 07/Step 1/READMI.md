
# Day 7: Bridge Repair

## Problem Overview

The Historians have guided you to a jungle rope bridge in need of urgent repairs. The engineers working on the bridge need your help solving calibration equations to complete their task. These equations have missing operators, and it is up to you to determine which combinations of operators make the equations valid.

Your goal is to determine which calibration equations are valid and compute the total of their test values.

---

## Task Description

### Problem Details

1. **Input Format**  
   Each calibration equation is presented as:
   - A test value (integer) before the colon (`:`).
   - A series of numbers (space-separated) after the colon.

   Example:  
   ```
   190: 10 19
   3267: 81 40 27
   ```

2. **Rules for Validity**  
   - Operators (`+` for addition and `*` for multiplication) must be inserted between the numbers in the exact order they are listed.
   - Operators are evaluated **left-to-right**, without precedence rules (e.g., `a + b * c` is evaluated as `(a + b) * c`).
   - If the result equals the test value, the equation is valid.

3. **Objective**  
   - Identify all valid equations.
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

The total calibration result is:  
`190 + 3267 + 292 = 3749`.

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
```

---

## Output Format

A single integer representing the total calibration result of all valid equations.