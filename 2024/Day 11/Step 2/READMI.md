# Day 11: Plutonian Pebbles - Part Two

## Problem Overview
Continue observing the stone transformation process, this time extending the observation to 75 blinks.

## Challenge Details
- Use the same stone transformation rules from Part One
- Determine the total number of stones after 75 consecutive blinks

## Transformation Rules (Recap)
1. **Zero Rule**: 
   - Stone marked `0` becomes `1`

2. **Even Digit Split Rule**:
   - Even-digit stones split into two stones
   - First half and second half of digits
   - Leading zeroes removed

3. **Multiplication Rule**:
   - Stones not matching other rules replaced
   - New stone's number = Original number * 2024

## Key Observations
- Stone order remains constant
- Transformations occur simultaneously
- Complexity increases exponentially with blink count

## Example Reference
- Part One showed dramatic growth:
  - Initial state: Few stones
  - 25 blinks: 55,312 stones
  - 75 blinks: Even more stones

## Challenge
Calculate the total number of stones after blinking 75 times.

## Input
- Initial line of stones with numbers
- Integer markings for each stone

## Output
- Total number of stones after 75 blinks