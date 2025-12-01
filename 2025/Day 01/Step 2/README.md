# Part Two: Method 0x434C49434B

## Problem Overview
The first password was rejected. A new security document reveals a stricter protocol ("Method 0x434C49434B") involving the mechanical "clicks" of the dial.

## Updated Scoring Rules
- **Objective:** Count the total number of times the dial points to `0`
- **Condition:** Count instances of `0` both:
  1. At the **end** of a rotation (as in Part 1)
  2. **During** a rotation (passing through `0`)

### The "Click" Concept
- Every single unit of rotation counts as a step.
- If a rotation moves the dial from `1` to `99` (via Left), it clicks on `0` in between.
- **Looping:** A very large rotation might cause the dial to pass `0` multiple times before stopping.

## Example Scenarios

### Detailed Trace (From Part 1 Input)
*Starting Position: `50`*

1. `L68` (Moves `50` -> `82`):
   - Passes through `0`.
   - **Hits:** 1

2. `L30` (Moves `82` -> `52`):
   - Does not pass `0`.
   - **Hits:** 0

3. `R48` (Moves `52` -> `0`):
   - Ends on `0`.
   - **Hits:** 1

4. `L5` (Moves `0` -> `95`):
   - Immediately moves off `0`.
   - **Hits:** 0

5. `R60` (Moves `95` -> `55`):
   - Passes through `0`.
   - **Hits:** 1

6. `L55` (Moves `55` -> `0`):
   - Ends on `0`.
   - **Hits:** 1

7. `L1` (Moves `0` -> `99`):
   - **Hits:** 0

8. `L99` (Moves `99` -> `0`):
   - Ends on `0`.
   - **Hits:** 1

9. `R14` (Moves `0` -> `14`):
   - **Hits:** 0

10. `L82` (Moves `14` -> `32`):
    - Passes through `0`.
    - **Hits:** 1

**Total Password:** 6

### Edge Case Warning

- Start: `50` 
- Rotation: `R1000`
- The dial rotates 1000 clicks to the right.
- The dial is a circle of 100 numbers.
- It completes 10 full circles (`1000 / 100 = 10`).
- It lands back on `50`.
- **Score:** It passed `0` exactly **10 times**.

## Challenge
Re-calculate the password using the new "Method 0x434C49434B" logic on the original input sequence.

## Input
- Same rotation sequence as Part One.

## Output
- Single integer representing the total count of `0` encounters.