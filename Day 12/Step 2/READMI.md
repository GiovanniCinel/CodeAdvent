# Garden Groups - Part Two

## Problem Overview
Calculate the total fencing cost using a new method that considers both region area and number of sides.

## New Pricing Method
- Price of each region = Area × Number of Sides
- Each straight section of fence counts as a side
- Sides can be on the outside or inside of a region

## Side Counting Rules
- Count all straight fence sections
- Fence sections do not connect across region boundaries
- Each section has an "in-side" and an "out-side"

## Example Scenarios

### Simple Region Example
```
AAAA
BBCD
BBCC
EEEC
```

Region Pricing:
- A: 4 sides, Area 4 → Price 16
- B: 4 sides, Area 4 → Price 16
- C: 8 sides, Area 4 → Price 32
- D: 4 sides, Area 1 → Price 4
- E: 4 sides, Area 3 → Price 12

**Total Price**: 80

### Complex Region Example
```
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
```

Region Pricing:
- E-shaped region: 
  - Area 17
  - 12 sides
  - Price: 17 × 12 = 204
- X regions: Separate calculations

**Total Price**: 236

### Intricate Region Example
```
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
```

Region Pricing:
- A region: 
  - Outer sides: 4
  - Inner sides: 8
  - Total sides: 12
  - Area calculation required
- B regions: Each with 4 sides

**Total Price**: 368

## Large Example Breakdown
```
(Complex map with multiple regions)
```

Region Pricing Examples:
- R plants: 12 × 10 = 120
- I plants: 4 × 4 = 16
- C plants: 14 × 22 = 308
- F plants: 10 × 12 = 120
- V plants: 13 × 10 = 130
- J plants: 11 × 12 = 132
- Additional C plants: 1 × 4 = 4
- E plants: 13 × 8 = 104
- Another I plants: 14 × 16 = 224
- M plants: 5 × 6 = 30
- S plants: 3 × 6 = 18

**Total Price**: 1206

## Challenge
Calculate the new total price of fencing all regions on the provided map.

## Input
- 2D grid representing plant regions
- Different letters representing different plant types

## Output
- Single integer representing the total fencing cost
- Calculated by multiplying each region's area by its number of sides
