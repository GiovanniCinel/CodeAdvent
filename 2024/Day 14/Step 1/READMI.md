# Day 14: Restroom Redoubt

## Problem Overview
Navigate and predict robot movements in a enclosed space to determine the safest area for The Historian to pass through.

## Space Characteristics
- Total Space: 101 tiles wide × 103 tiles tall
- Wrapping Edges: Robots teleport to opposite side when hitting boundaries

## Robot Information Input
### Position Format
- `p=x,y`
- `x`: Tiles from left wall
- `y`: Tiles from top wall
- Example: `p=0,4` = Top-left quadrant, 4 tiles down

### Velocity Format
- `v=x,y`
- `x`: Horizontal movement (tiles/second)
  - Positive: Moving right
  - Negative: Moving left
- `y`: Vertical movement (tiles/second)
  - Positive: Moving down
  - Negative: Moving up
- Example: `v=1,-2` = 1 tile right, 2 tiles up per second

## Movement Rules
- Robots move in straight lines
- Can occupy same tile without interaction
- Teleport when reaching space boundaries
- Wrap around to opposite side of the space

## Safety Factor Calculation
1. Simulate robot positions after 100 seconds
2. Count robots in each quadrant
3. Multiply quadrant robot counts

### Quadrant Rules
- Exclude robots on exact center lines
- Calculate robots in four quadrants

## Example Simulation

### Initial Robot Positions
```
p=2,4 v=2,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
```

### Movement Demonstration
```
Initial State:
...........
...........
...........
...........
..1........
...........
...........

After 1 Second:
...........
....1......
...........
...........
...........
...........
...........
```

### Quadrant Robot Count
```
Quadrants after 100 seconds:
..... 2..1.
..... .....
1.... .....
           
..... .....
...12 .....
.1... 1....

Quadrant Counts:
- Top Left: 1 robot
- Top Right: 3 robots
- Bottom Left: 4 robots
- Bottom Right: 1 robot

Safety Factor: 1 × 3 × 4 × 1 = 12
```

## Challenge
- Calculate the safety factor after exactly 100 seconds
- Predict robot positions in 101×103 tile space

## Input
- List of robot initial positions and velocities
- Format: `p=x,y v=x,y`

## Output
- Single integer representing the safety factor
