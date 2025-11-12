# Day 11: Plutonian Pebbles

## Problem Overview
Analyze the evolution of a line of stones with unique transformation rules during each "blink".

## Stone Transformation Rules
When a blink occurs, stones transform simultaneously according to these rules (in order):

1. **Zero Rule**
   - If a stone is engraved with `0`, it becomes a stone marked `1`

2. **Even Digit Split Rule**
   - If a stone has an *even number of digits*:
     - Split into two stones
     - Left stone: First half of the digits
     - Right stone: Second half of the digits
     - Leading zeroes are dropped

3. **Multiplication Rule**
   - If no other rules apply:
     - Replace the stone with a new stone
     - New stone's number = Original number * 2024

## Key Characteristics
- Stone order is always preserved
- Transformations happen simultaneously
- Line of stones remains in a straight line

## Example Walkthrough
### Initial Arrangement: `0 1 10 99 999`

#### After First Blink
- `0` → `1`
- `1` → `2024`
- `10` → `1 0`
- `99` → `9 9`
- `999` → `2021976`

**Result**: `1 2024 1 0 9 9 2021976`

### Extended Example
```
Initial: 125 17
Blink 1: 253000 1 7
Blink 2: 253 0 2024 14168
Blink 3: 512072 1 20 24 28676032
Blink 4: 512 72 2024 2 0 2 4 2867 6032
Blink 5: 1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32
Blink 6: 2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2
```

**Observations**:
- Blink 1: 7 stones
- Blink 6: 22 stones
- Blink 25: 55,312 stones

## Challenge
Determine the number of stones after blinking 25 times, starting with the given initial arrangement.

## Input
- Initial line of stones with numbers
- Integers representing stone markings

## Output
- Total number of stones after 25 blinks