# Day 2: Gift Shop

## Problem Overview
Assist the Gift Shop clerks in cleaning up a corrupted database by identifying and summing specific "invalid" product IDs within given numerical ranges.

## The Pattern Rule
An ID is considered **Invalid** if it consists strictly of a sequence of digits repeated exactly twice.

### Logic Definition
- Let the ID be a string `S`.
- `S` is invalid if it can be split into two identical halves `A + A`.
- Consequently, the length of the ID must always be **even**.

### Valid vs Invalid Examples
- **Invalid (Target):**
  - `55` -> `5` repeated twice.
  - `6464` -> `64` repeated twice.
  - `123123` -> `123` repeated twice.
- **Valid (Ignore):**
  - `101` -> Cannot be split into two identical halves.
  - `0101` -> Numbers cannot have leading zeros (not a valid ID format).
  - `1213` -> First half `12` does not match second half `13`.

## Input Format
- A single line of text containing multiple numerical ranges separated by commas.
- Format: `StartID-EndID`
- Example: `11-22,95-115,998-1012`

## Task Execution
1. Parse the input to get start and end points for each range (inclusive).
2. Iterate through every number in those ranges.
3. Check if the number satisfies the "repeated sequence" pattern.
4. Keep a running sum of all numbers that satisfy the pattern.

## Example Scenario

### Input Ranges

```
11-22, 95-115, 998-1012, 1188511880-1188511890, 222220-222224, 1698522-1698528, 446443-446449, 38593856-38593862
```

### Analysis
| Range | Found Invalid ID | Pattern |
| :--- | :--- | :--- |
| `11-22` | **11** | `1` repeated |
| `11-22` | **22** | `2` repeated |
| `95-115` | **99** | `9` repeated |
| `998-1012` | **1010** | `10` repeated |
| `1188511880-1188511890` | **1188511885** | `11885` repeated |
| `222220-222224` | **222222** | `222` repeated |
| `1698522-1698528` | *(None)* | - |
| `446443-446449` | **446446** | `446` repeated |
| `38593856-38593862` | **38593859** | `3859` repeated |

### Calculation
- Sum of found IDs: `11 + 22 + 99 + 1010 + 1188511885 + 222222 + 446446 + 38593859`
- **Total:** `1227775554`

## Challenge
Find all invalid IDs in your specific puzzle input ranges and calculate their sum.

## Input
- A comma-separated list of ranges (e.g., `10-20,40-50`).

## Output
- A single integer representing the sum of all invalid IDs found.