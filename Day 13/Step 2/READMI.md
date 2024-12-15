# Day 13: Claw Contraption - Part Two

## Problem Overview
Recalibrate the prize coordinates due to a significant unit conversion error, dramatically changing the prize locations and winning conditions.

## Coordinate Adjustment
- Add `10000000000000` to both X and Y coordinates of every prize
- Dramatically shifts prize positions
- Significantly reduces the number of winnable prizes

## Coordinate Transformation Example

### Before Correction
```
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
```

### After Correction
```
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=10000000008400, Y=10000000005400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=10000000012748, Y=10000000012176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=10000000007870, Y=10000000006450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=10000000018641, Y=10000000010279
```

## Key Observations
- Only second and fourth claw machines now have winnable prizes
- Winning all prizes requires many more than 100 button presses
- Significant computational challenge to determine optimal strategy

## Challenge
- Determine the fewest tokens needed to win all possible prizes
- Account for the massive coordinate shift
- Optimize button press sequence

## Input
- Claw machine button press sequences
- Button press coordinates
- Prize locations

## Output
- Minimum number of tokens required to win all possible prizes
