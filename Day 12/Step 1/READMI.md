# Day 12: Garden Groups

## Problem Overview
Calculate the total fencing cost for garden plot regions in a complex agricultural landscape.

## Key Concepts

### Garden Plot Regions
- Each plot grows a single type of plant (identified by a letter)
- Regions formed by adjacent plots of the same type
- Adjacent plots connect horizontally or vertically

## Calculation Parameters

### Region Area
- Number of garden plots in the region
- Counted by unique plot instances of the same type

### Region Perimeter
- Sides of plots not touching another plot of the same type
- Measured by external and internal boundaries

### Fencing Price
- Calculated as: `Region Area * Region Perimeter`
- Total map cost = Sum of individual region fencing prices

## Example Analysis

### Simple Example
```
AAAA
BBCD
BBCC
EEEC
```

#### Region Breakdown
- Type A: Area 4, Perimeter 10, Price = 4 * 10 = 40
- Type B: Area 4, Perimeter 8, Price = 4 * 8 = 32
- Type C: Area 4, Perimeter 10, Price = 4 * 10 = 40
- Type D: Area 1, Perimeter 4, Price = 1 * 4 = 4
- Type E: Area 3, Perimeter 8, Price = 3 * 8 = 24

**Total Price**: 140

### Complex Example
```
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
```

#### Region Breakdown
- O Region: Area 21, Perimeter 36, Price = 21 * 36 = 756
- X Regions: Each Area 1, Perimeter 4, Price = 1 * 4 = 4

**Total Price**: 772

### Large Example
```
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
```

#### Notable Regions
- R Plants: Area 12, Perimeter 18, Price = 216
- C Plants: Area 14, Perimeter 28, Price = 392
- J Plants: Area 11, Perimeter 20, Price = 220
- E Plants: Area 13, Perimeter 18, Price = 234

**Total Price**: 1930

## Challenge
Calculate the total fencing price for all regions in the provided garden plot map.

## Input
- 2D grid of characters
- Each character represents a garden plot type

## Output
- Single integer representing total fencing cost
