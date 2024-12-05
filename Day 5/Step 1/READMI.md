
# Day 5: Print Priority Puzzle

## Problem Overview

The Historians, continuing their quest for order amidst the chaos of sub-basement 17, now face another challenge in the North Pole printing department. A familiar Elf has tasked you with verifying that updates to the sleigh launch safety manuals are printed in the correct order.

Failure to maintain proper ordering of pages could lead to catastrophic consequences for the upcoming Christmas season. Your goal is to determine which updates are in the correct order and calculate a summary statistic based on their "middle page numbers."

---

## Task Description

### Problem Details

The printing task comes with **page ordering rules** and **update sequences**:

1. **Page Ordering Rules**  
   Each rule is provided in the form `X|Y`, meaning that if both page `X` and page `Y` are included in an update, then `X` must appear **before** `Y`.  
   Example:  
   ```
   47|53
   97|13
   ```
   Here, `47` must come before `53`, and `97` must come before `13` in any valid update.

2. **Update Sequences**  
   Each update consists of a list of page numbers, provided in the order they are meant to be printed.  
   Example:  
   ```
   75,47,61,53,29
   97,61,53,29,13
   ```

   The task is to verify whether each update respects the provided ordering rules.

---

### Solution Requirements

For each update:
1. **Determine Validity:** Check if the update respects all the relevant ordering rules.  
   - Ignore rules involving page numbers that do not appear in the update.  
   - Validate that for every rule `X|Y`, page `X` appears **before** page `Y` in the update.

2. **Calculate Middle Page Numbers:** If an update is valid, find its "middle page number":  
   - For updates with an odd number of pages, the middle page is the one at the exact center.  
   - For updates with an even number of pages, choose the lower-indexed middle page.

3. **Sum Middle Page Numbers:** Add up the middle page numbers from all valid updates.

---

## Example Walkthrough

### Input

**Page Ordering Rules:**  
```
47|53  
97|13  
97|61  
75|29  
... (and more)
```

**Update Sequences:**  
```
75,47,61,53,29  
97,61,53,29,13  
75,29,13  
75,97,47,61,53  
...
```

### Output

- Determine which updates are in the correct order:
  - **Valid Updates:**  
    ```
    75,47,61,53,29 -> Middle Page: 61  
    97,61,53,29,13 -> Middle Page: 53  
    75,29,13       -> Middle Page: 29  
    ```
  - **Invalid Updates:**  
    ```
    75,97,47,61,53 -> Invalid (violates rule 97|75)
    ...
    ```

- Sum of middle pages: `61 + 53 + 29 = 143`.

---

## Input Format

1. **Page Ordering Rules:**  
   A list of rules in the format `X|Y`, separated by newlines.

2. **Update Sequences:**  
   A list of updates, where each update is a comma-separated sequence of page numbers.

---

## Output Format

- A single integer: the sum of the middle page numbers for all valid updates.
