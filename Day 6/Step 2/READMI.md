# Day 6: Guard Gallivant - Part Two
## Problem Overview
After tracking the guard's initial movement path, The Historians propose introducing a single new obstruction to create a situation where the guard becomes trapped in a permanent patrol loop. Your task is to determine how many unique positions could effectively trap the guard without causing a time paradox.
---
## Task Description
### Problem Details
The challenge involves strategically placing a new obstacle to create a guard movement loop:
1. **Placement Constraints**  
   - Cannot place the obstruction at the guard's starting position
   - Must result in a definitive movement loop
   - Minimal impact on the overall lab environment
2. **Obstruction Representation**  
   Obstacles are marked with different symbols indicating movement patterns:
   - `O`: New obstruction position
   - `|`: Vertical movement area
   - `-`: Horizontal movement area
   - `+`: Intersectional movement area
---
### Solution Requirements
1. **Loop Detection**  
   - Identify positions where a new obstruction causes repetitive guard movement
   - Ensure the guard cannot escape the defined area
2. **Unique Position Counting**  
   - Count distinct obstruction locations that create a movement loop
   - Prioritize solutions with minimal time paradox risk
---
## Example Walkthrough
### Input
**Initial Map:**  
```
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
........#.
#.........
......#...
```
### Potential Obstruction Scenarios
1. **Printing Press Placement**  
   ```
   .#.O^---+.
   ```
2. **Suit Prototype Stack**  
   ```
   .#+-^-+-+.
   ......O.#.
   ```
3. **Chimney-Squeeze Fabric**  
   ```
   .#+-^-+-+.
   .+----+O#.
   ```
### Output
- Total unique loop-creating obstruction positions: `6`
---
## Input Format
1. **Grid Map:**  
   - Rectangular grid representing lab layout
   - Guard's starting position marked
   - Existing obstacles defined
2. **Movement Rules:**  
   - Turn right at obstacles
   - Move forward when path is clear
---
## Output Format
- Single integer: number of positions where a new obstruction creates a guard movement loop
