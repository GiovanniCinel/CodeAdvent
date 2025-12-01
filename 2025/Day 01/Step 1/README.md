# Day 1: Secret Entrance

## Problem Overview
Decipher the logic of a circular safe dial to reveal the actual password required to enter the North Pole base.

## Dial Mechanics
- The safe dial contains numbers from `0` through `99` in a circle
- **Starting Position:** The dial begins pointing at `50`
- **Circular Movement:**
  - Rotating **Left** from `0` moves to `99`
  - Rotating **Right** from `99` moves to `0`

## Rotation Instructions
- Input consists of a list of rotations (one per line)
- Format: A direction (`L` or `R`) followed by a distance value
  - `L`: Rotate **Left** (towards lower numbers)
  - `R`: Rotate **Right** (towards higher numbers)

### Calculation Rules
- Apply the rotation distance to the current position
- Handle the wrap-around (modulo 100)
- Example: If at `11`, `R8` points to `19`
- Example: If at `5`, `L10` points to `95`

## The Password Logic
- The safe is a decoy; the open status is irrelevant
- **Password** = The total count of times the dial lands exactly on `0` after a rotation is complete

## Example Scenario

### Input Sequence
```
L68 
L30 
R48 
L5 
R60
L55 
L1 
L99 
R14 
L82
```

### Execution Trace
- **Start:** `50`
1. `L68`: `50` -> Left 68 -> **`82`**
2. `L30`: `82` -> Left 30 -> **`52`**
3. `R48`: `52` -> Right 48 -> **`0`** (Match! Count: 1)
4. `L5`:  `0`  -> Left 5  -> **`95`**
5. `R60`: `95` -> Right 60 -> **`55`**
6. `L55`: `55` -> Left 55 -> **`0`** (Match! Count: 2)
7. `L1`:  `0`  -> Left 1  -> **`99`**
8. `L99`: `99` -> Left 99 -> **`0`** (Match! Count: 3)
9. `R14`: `0`  -> Right 14 -> **`14`**
10. `L82`: `14` -> Left 82 -> **`32`**

- **Total Score:** 3

## Challenge
Analyze the full sequence of rotations in your puzzle input.

## Input
- List of strings representing rotations (e.g., `L68`, `R12`)
- Start position is always `50`

## Output
- Single integer representing the number of times the dial points to `0`