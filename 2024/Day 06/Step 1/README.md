# Day 6: Guard Gallivant
## Problem Overview
The Historians have transported you to the North Pole prototype suit manufacturing lab in 1518. A guard is patrolling the area, and your task is to predict her movement path through the lab. Your goal is to determine the number of distinct positions the guard will visit before leaving the mapped area.
Careful tracking is crucial to ensure the Historians can safely search the lab without encountering the guard. Understanding the guard's precise movement pattern will reveal the exact positions at risk during their investigation.
---
## Task Description
### Problem Details
The guard's movement follows a strict patrol protocol with two simple rules:
1. **Obstacle Handling**  
   If there is something directly in front of the guard, turn right 90 degrees.  
   Example:  
   ```
   ....#.....
   ....^....#
   ```
   When the guard encounters the `#` obstacle, she turns right.
2. **Movement Protocol**  
   If the path ahead is clear, take one step forward in the current direction.  
   Example:  
   ```
   ....#.....
   .........#
   ..#.......
   .#..^.....
   ```
   The guard moves forward when no obstacles block her path.
---
### Solution Requirements
For tracking the guard's path:
1. **Movement Tracking:** Follow the guard's movement through the grid.  
   - Start from the initial position marked with `^`
   - Apply movement rules consistently
   - Track each unique position visited
2. **Position Counting:** Determine the total number of distinct positions.  
   - Include the starting position
   - Count each unique grid location visited
3. **Path Termination:** Stop counting when the guard leaves the mapped area.
---
## Example Walkthrough
### Input
**Initial Map:**  
```
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
```
**Movement Sequence:**  
```
Initial: Guard facing up
First moves: Advance until obstacle
Turn right at obstacle
Continue in new direction
```
### Output
- Trace the guard's path through the grid
- **Visited Positions:**  
  ```
  ....#.....
  ....XXXXX#
  ....X...X.
  ..#.X...X.
  ..XXXXX#X.
  ..X.X.X.X.
  .#XXXXXXX.
  .XXXXXXX#.
  #XXXXXXX..
  ......#X..
  ```
- Total unique positions visited: `41`
---
## Input Format
1. **Grid Map:**  
   A 2D grid representing the lab layout
   - `^` indicates initial guard position
   - `#` represents obstacles
   - `.` represents open spaces
2. **Grid Constraints:**  
   - Rectangular grid
   - Finite mapped area
---
## Output Format
- A single integer: the number of distinct positions visited by the guard
