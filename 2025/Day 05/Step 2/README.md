# Day 5: Cafeteria - Part Two

## Problem Overview
The inventory cleanup shifts focus. The "Available IDs" list is discarded. The goal is now to calculate the sheer volume of the "Fresh" zone defined by the ranges.

## The Objective
Calculate the total count of **unique** integer IDs that fall into **any** of the provided fresh ingredient ranges.

## Logic: Merging Intervals
Since ranges can overlap, simply summing their lengths would result in duplicates.
- **Rule:** If range A (`10-14`) and range B (`12-18`) overlap, they form a single continuous range (`10-18`).
- **Calculation:** You must merge all overlapping ranges first, then sum the lengths of the resulting disjoint intervals.

### The "Available IDs" Section
- **Status:** Irrelevant.
- **Action:** Ignore the second part of the input file entirely.

## Example Scenario

### Input Ranges

```
3-5 
10-14 
16-20 
12-18
```
### Trace: Merging Process
1.  **Sort Ranges by Start ID:**
    - `3-5`
    - `10-14`
    - `12-18`
    - `16-20`

2.  **Merge Step-by-Step:**
    - `3-5`: No overlap with next (`10`). Keep as is.
    - `10-14` vs `12-18`:
        - They overlap (12 is inside 10-14).
        - New end is max(14, 18) = 18.
        - **Merged:** `10-18`.
    - `10-18` (current) vs `16-20`:
        - They overlap (16 is inside 10-18).
        - New end is max(18, 20) = 20.
        - **Merged:** `10-20`.

3.  **Final Disjoint Intervals:**
    - Range A: `3-5`
    - Range B: `10-20`

### Calculation
- **Range A (`3-5`):** Count = `5 - 3 + 1` = **3** IDs.
- **Range B (`10-20`):** Count = `20 - 10 + 1` = **11** IDs.
- **Total:** `3 + 11` = **14**.

## Challenge
Process the "Fresh Ingredient ID Ranges" from your input. Merge overlaps and calculate the total number of unique IDs covered.

## Input
- The first section of the input file (ranges like `Start-End`).

## Output
- A single integer representing the total count of fresh IDs.
  *(Note: This number can be very large, potentially exceeding standard 32-bit integer limits).*