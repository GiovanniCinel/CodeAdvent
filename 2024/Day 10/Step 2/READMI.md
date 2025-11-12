# Day 10: Hoof It - Part Two

## Problem Overview
Discover a new method of measuring trailhead significance based on the number of distinct hiking trails originating from each trailhead.

## Trailhead Rating Concept
- A trailhead's rating is the total number of *distinct hiking trails* that begin at that position
- Distinct trails are unique paths that reach different `9`-height destinations

## Hiking Trail Rules (Unchanged)
- Start at height `0`
- End at height `9`
- Increase by exactly 1 at each step
- Move only up, down, left, or right (no diagonals)

## Example Scenarios

### Simple Trailhead Rating
```
.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....
```
- Trailhead: Top right
- Rating: 3 distinct hiking trails
  - Different trails reaching various destinations

### Advanced Trailhead Rating
```
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
```
- Single trailhead
- Rating: 13 distinct hiking trails

### Complex Trailhead Rating
```
012345
123456
234567
345678
4.6789
56789.
```
- Single trailhead
- Rating: 227 distinct hiking trails
  - 121 trails to right-edge `9`
  - 106 trails to bottom-edge `9`

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
- Trailhead ratings in reading order:
  - 20, 24, 10, 4, 1, 4, 5, 8, 5
- Total sum of trailhead ratings: 81

## Challenge
Calculate the sum of ratings for all trailheads on the provided topographic map.

## Input
- 2D grid representing terrain heights
- Heights range from `0` to `9`

## Output
- Single integer representing the total trailhead ratings sum
