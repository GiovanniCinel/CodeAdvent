# Day 10: Hoof It

## Problem Overview
Explore a topographic map and calculate the total score of all trailheads in a hiking landscape.

## Terrain Rules
- Map represents terrain heights from `0` (lowest) to `9` (highest)
- Hiking trails must:
  - Start at height `0`
  - End at height `9`
  - Increase by exactly 1 at each step
  - Move only up, down, left, or right (no diagonals)

## Trailhead Concept
- A trailhead is any position with height `0`
- Trailhead score = Number of `9`-height positions reachable via valid hiking trails

### Trailhead Scoring Rules
- Count reachable `9` positions through valid hiking trails
- Only count positions reached by incrementing exactly 1 at each step
- Impassable tiles (`.`) may block potential paths

## Example Scenarios

### Simple Trailhead Example
```
...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
```
- Trailhead: Top center
- Score: 2 reachable `9` positions

### Complex Trailhead Example
```
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
```
- Trailhead: Specific position
- Score: 4 reachable `9` positions (except one)

### Multiple Trailheads
```
10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01
```
- Two trailheads
- Top trailhead score: 1
- Bottom trailhead score: 2

## Large Example
```
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
```
- 9 trailheads
- Trailhead scores: 5, 6, 5, 3, 1, 3, 5, 3, 5
- Total score: 36

## Challenge
Calculate the sum of scores for all trailheads on the provided topographic map.

## Input
- 2D grid representing terrain heights
- Heights range from `0` to `9`

## Output
- Single integer representing the total trailhead score
