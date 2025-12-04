# Day 4: Printing Department

## Problem Overview
Optimize forklift operations to break through a wall by identifying which paper rolls in a crowded warehouse grid are "accessible".

## Grid Legend
- The warehouse is represented as a 2D grid of characters.
- `@`: A roll of paper.
- `.`: Empty floor space.

## Access Rules
A specific roll of paper (`@`) is considered **accessible** to a forklift only if it meets a specific density condition.

### The Condition
- **Target:** Check every `@` on the grid.
- **Rule:** The roll is accessible if there are **fewer than 4** other rolls (`@`) in its 8 adjacent positions.
- **Neighbors:** Inspect Up, Down, Left, Right, and the 4 Diagonals.
- **Boundaries:** Positions outside the grid count as empty (not rolls).

## Example Scenario

### Raw Grid

```
..@@.@@@@. 
@@@.@.@.@@ 
@@@@@.@.@@ 
@.@@@@..@. 
@@.@@@@.@@ 
.@@@@@@@.@ 
.@.@.@.@@@ 
@.@@@.@@@@ 
.@@@@@@@@. 
@.@.@@@.@.
```

### Visualization of Accessible Rolls (`x`)
*Note: `x` indicates a roll that had < 4 neighbors.*

```
..xx.xx@x. 
x@@.@.@.@@ 
@@@@@.x.@@ 
@.@@@@..@. 
x@.@@@@.@x 
.@@@@@@@.@ 
.@.@.@.@@@ 
x.@@@.@@@@ 
.@@@@@@@@. 
x.x.@@@.x.
```

### Result
- Count of `x` marks: **13**

## Challenge
Analyze the complete warehouse map. Determine the total number of paper rolls that are accessible to the forklifts.

## Input
- A block of text representing the grid rows.

## Output
- A single integer representing the count of accessible paper rolls.