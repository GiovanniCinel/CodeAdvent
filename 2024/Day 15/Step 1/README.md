# Day 15: Warehouse Woes

## Problem Overview
You're helping lanternfish manage a warehouse where a robot is moving boxes, with complex and unpredictable movement rules.

## Scenario
- A robot is moving through a warehouse, attempting to push boxes
- Lanternfish need help tracking the robot's movements and final box positions

## Game Map
- `#`: Walls
- `@`: Robot's starting position
- `O`: Boxes
- `.`: Empty spaces

## Movement Rules
1. Robot moves in four directions: `^` (up), `v` (down), `<` (left), `>` (right)
2. When moving, the robot attempts to push boxes in its path
3. If a move would cause the robot or a box to hit a wall, *nothing moves*

## GPS Coordinate Calculation
- Coordinate = `(100 * distance_from_top) + distance_from_left`
- Measured from top-left corner of the map
- Calculation continues past wall tiles to map edges

### Coordinate Calculation Example
```
#######
#...O..
#......
```
- Box is 1 unit from top, 4 units from left
- GPS Coordinate: `(100 * 1) + 4 = 104`

## Challenge Objective
1. Simulate robot's movement through the warehouse
2. Track final positions of all boxes
3. Calculate sum of boxes' GPS coordinates

## Examples

### Small Example
#### Initial State
```
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
```

#### Moves
`<^^>>>vv<v>>v<<`

#### Final State
```
########
#.....O#
##.....#
#...@..#
#.#....#
#......#
#......#
########
```

### Large Example
#### Sum of GPS Coordinates: 10,092

## Input
- Warehouse map representing initial state
- Sequence of moves for the robot

## Output
- Sum of all boxes' GPS coordinates after robot's movements
