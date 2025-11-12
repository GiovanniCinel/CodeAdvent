# Day 15: Warehouse Woes - Part Two

## Problem Overview
A second warehouse with a similar layout to the first, but with a key difference: everything except the robot is *twice as wide*.

## Map Scaling Rules
When scaling the original map, transform each tile as follows:

| Original Tile | Scaled Tile |
|--------------|-------------|
| `#` (Wall)   | `##`        |
| `O` (Box)    | `[]`        |
| `.` (Empty)  | `..`        |
| `@` (Robot)  | `@.`        |

### Important Notes
- Robot remains the same size and speed
- Boxes are now two tiles wide
- Total map width and height increase
- Original movement sequence remains unchanged

## GPS Coordinate Calculation
- Measure from map edge to the closest edge of the box
- Formula: `100 * (distance_from_top) + (distance_from_left)`

### Coordinate Calculation Example
```
##########
##...[]...
##........
```
- Box is 1 unit from top, 5 units from left
- GPS Coordinate: `(100 * 1) + 5 = 105`

## Movement Rules
1. Robot moves in four directions: `^` (up), `v` (down), `<` (left), `>` (right)
2. Wide boxes can push two boxes simultaneously
3. Walls block movement completely
4. Some moves might not change the map's state

## Challenge Objective
1. Scale up the original warehouse map
2. Simulate robot's movement through the scaled warehouse
3. Track final positions of all boxes
4. Calculate sum of boxes' GPS coordinates


## Key Differences from Part One
- Map is twice as wide
- Boxes represented by `[]`
- GPS coordinate calculation slightly modified
- Robot movement remains the same
- More complex box pushing interactions possible

## Example Scenario
### Initial State
```
####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################
```

### Final State
```
####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################
```

### GPS Coordinate Sum: 9,021

## Input
- Original warehouse map
- Original robot movement sequence

## Output
- Sum of all wide boxes' GPS coordinates after robot's movements
