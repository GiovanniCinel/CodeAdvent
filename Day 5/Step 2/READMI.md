
# Day 5: Print Priority Puzzle - Part Two

## Problem Overview

While the Elves work on printing the correctly-ordered updates, you are tasked with fixing the updates that are **not** in the correct order. Using the provided page ordering rules, reorder the pages in each invalid update to make them valid.

After reordering the invalid updates, calculate a summary statistic based on their "middle page numbers."

---

## Task Description

### Problem Details

The problem involves **page ordering rules** and **update sequences**, just like in Part One. However, for this task, the focus is on the **incorrectly-ordered updates**.

1. **Page Ordering Rules**  
   The same rules apply: Each rule `X|Y` indicates that if both page `X` and page `Y` are included in an update, then `X` must appear **before** `Y`.  
   Example:  
   ```
   47|53
   97|13
   ```

2. **Incorrect Updates**  
   Your task is to reorder the pages in each incorrectly-ordered update to satisfy all the applicable page ordering rules.

---

### Solution Requirements

For each incorrectly-ordered update:
1. **Reorder Pages:** Rearrange the pages to satisfy all the relevant ordering rules.
   - Rules involving missing pages in the update are ignored.
   - Ensure that for every rule `X|Y`, page `X` appears **before** page `Y`.

2. **Calculate Middle Page Numbers:** For each reordered update, determine the "middle page number":
   - For updates with an odd number of pages, the middle page is the one at the exact center.  
   - For updates with an even number of pages, choose the lower-indexed middle page.

3. **Sum Middle Page Numbers:** Add up the middle page numbers from all reordered updates.

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
61,13,29  
97,13,75,29,47  
```

### Output

- Determine which updates are invalid and reorder them:
  - **Reordered Updates:**  
    ```
    75,97,47,61,53 -> Reordered: 97,75,47,61,53 (Middle Page: 47)  
    61,13,29       -> Reordered: 61,29,13       (Middle Page: 29)  
    97,13,75,29,47 -> Reordered: 97,75,47,29,13 (Middle Page: 47)  
    ```

- Sum of middle pages for reordered updates: `47 + 29 + 47 = 123`.

---

## Input Format

1. **Page Ordering Rules:**  
   A list of rules in the format `X|Y`, separated by newlines.

2. **Update Sequences:**  
   A list of updates, where each update is a comma-separated sequence of page numbers.

---

## Output Format

- A single integer: the sum of the middle page numbers for all reordered updates.
