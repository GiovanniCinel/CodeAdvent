# Day 5: Cafeteria

## Problem Overview
The Elves in the cafeteria are struggling with a new inventory system. You need to help them filter a list of ingredients to distinguish which are **Fresh** and which are **Spoiled**.

## Inventory Rules
The database defines freshness based on numerical ID ranges.

- **Fresh Ingredient:** An ID that falls inside **at least one** of the provided "Fresh ID Ranges".
- **Spoiled Ingredient:** An ID that does not fall into any of the ranges.
- **Range Behavior:**
  - Ranges are **inclusive** (e.g., `3-5` includes 3, 4, and 5).
  - Ranges can **overlap** (being in multiple ranges doesn't change the status; it's still just "Fresh").

## Input Format
The input file is divided into two distinct sections separated by a **blank line**.

1.  **Section 1: Fresh Ranges**
    - Format: `StartID-EndID`
    - Example: `3-5`
2.  **Blank Line**
3.  **Section 2: Available IDs**
    - A list of single integers (one per line) representing the ingredients currently in the kitchen.

## Example Scenario

### Input Data

```
3-5 
10-14 
16-20 
12-18

1 
5 
8 
11 
17 
32
```

### Analysis
- **Ranges:** `[3, 5]`, `[10, 14]`, `[16, 20]`, `[12, 18]`

**Check Process:**
- ID `1`: Not in any range -> **Spoiled**
- ID `5`: Inside `3-5` -> **Fresh**
- ID `8`: Not in any range -> **Spoiled**
- ID `11`: Inside `10-14` -> **Fresh**
- ID `17`: Inside `16-20` AND `12-18` -> **Fresh** (Overlaps are fine)
- ID `32`: Not in any range -> **Spoiled**

- **Total Fresh Count:** 3

## Challenge
Process the full database. Count how many of the "Available IDs" (Section 2) are valid according to the "Fresh Ranges" (Section 1).

## Output
- A single integer representing the count of fresh ingredients.