# Day 13: Claw Contraption

## Problem Overview
Optimize token spending to win prizes in unique claw machines with specialized movement buttons.

## Game Mechanics
- Two buttons: `A` and `B`
- Button costs:
  - Button `A`: 3 tokens
  - Button `B`: 1 token
- Each button moves claw in specific X and Y coordinates

## Prize Winning Conditions
- Must align claw exactly with prize coordinates
- Winning requires precise button press combinations
- Maximum 100 button presses per prize

## Button Press Calculation
- Calculate total X and Y movements
- Find minimum token-cost combination to reach prize

### Example Machine Breakdown

#### Machine 1
- Button A: `+94X, +34Y`
- Button B: `+22X, +67Y`
- Prize Location: `X=8400, Y=5400`
- Optimal Solution:
  - `A` button: 80 presses
  - `B` button: 40 presses
  - Total token cost: 280 tokens
  - Verification:
    - X: `(80 * 94) + (40 * 22) = 8400`
    - Y: `(80 * 34) + (40 * 67) = 5400`

#### Machine 2 and 4
- No possible prize-winning combination

#### Machine 3
- Optimal Solution:
  - `A` button: 38 presses
  - `B` button: 86 presses
  - Total token cost: 200 tokens

## Global Strategy
- Maximize number of prizes won
- Minimize total token expenditure
- Constraint: ≤ 100 button presses per prize

## Challenge Requirements
- Input: Claw machine button configurations and prize locations
- Goal: Find fewest tokens to win maximum prizes
- Button press limit: 100 per prize

## Input Format
- Multiple machines with:
  - Button A movement
  - Button B movement
  - Prize coordinates

## Output
- Minimum token count to win all possible prizes
