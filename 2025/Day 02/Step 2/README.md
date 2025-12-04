# Day 2: Gift Shop - Part Two

## Problem Overview
The database corruption is more extensive than initially thought. The "silly pattern" rule has evolved from strict double repetition to **any** multiple repetition.

## Updated Pattern Rules
An ID is now considered **Invalid** if it consists of a sequence of digits repeated **at least twice**.

### Logic Definition
- Let the ID be a string `S`.
- `S` is invalid if it is formed by repeating a substring `P`, `N` times.
- Condition: `N >= 2`.
- Unlike Part 1, the length of the ID does not strictly have to be even (e.g., `111` is length 3).

### Examples of New Invalid IDs
- `12341234` -> `1234` repeated **2** times (Part 1 compliant).
- `123123123` -> `123` repeated **3** times (New!).
- `1212121212` -> `12` repeated **5** times (New!).
- `1111111` -> `1` repeated **7** times (New!).

## Example Scenario Re-evaluation

Using the same ranges as Part 1, the results have changed:

| Range | New Invalid IDs | Reasoning |
| :--- | :--- | :--- |
| `11-22` | `11`, `22` | Unchanged (2x repetition). |
| `95-115` | **`99`**, **`111`** | `99` (2x `9`), `111` (3x `1`). |
| `998-1012` | **`999`**, **`1010`** | `999` (3x `9`), `1010` (2x `10`). |
| `565653-565659` | **`565656`** | `56` repeated 3 times. |
| `824824821...` | **`824824824`** | `824` repeated 3 times. |
| `2121212118...` | **`2121212121`** | `21` repeated 5 times. |

### Calculation Update
- Previous Sum (Part 1 Rules): `1,227,775,554`
- **New Sum (Extended Rules):** `4,174,379,265`

## Challenge
Re-scan the provided input ranges using the "at least twice" repetition rule. Find all invalid IDs and sum them up.

## Input
- Same comma-separated list of ranges as Part 1.

## Output
- Single integer representing the new total sum.