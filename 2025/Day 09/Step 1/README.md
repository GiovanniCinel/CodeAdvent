# Day 9: Movie Theater

## Problem Overview
You land in a movie theater with a tiled floor. The Elves are
redecorating and have marked specific tiles as 'red'.
Your goal is to identify the **largest possible rectangle** that can be
formed using these red tiles as anchors.

## The Rules
- **Input:** A list of coordinates `X,Y` representing red tiles.
- **Definition of Rectangle:**
  - You must choose exactly **two** red tiles from your list.
  - These two tiles serve as **opposite corners** of the rectangle.
  - The other two corners do *not* need to be red tiles (they can be
    empty space).
- **Objective:** Maximize the **Area** of this rectangle.

## Area Calculation (Crucial)
Based on the examples provided, the area is calculated **inclusively**
(counting the tiles themselves).

Formula given two points $(x_1, y_1)$ and $(x_2, y_2)$:
- **Width:** `|x1 - x2| + 1`
- **Height:** `|y1 - y2| + 1`
- **Area:** `Width * Height`

## Example Scenarios

### Scenario A: Area 24
Using corners `2,5` and `9,7`:
- Width: `|9 - 2| + 1 = 8`
- Height: `|7 - 5| + 1 = 3`
- Area: `8 * 3 = 24`
```
..............
.......#...#..
..............
..#....#......
..............
..OOOOOOOO....  <-- 3 rows high
..OOOOOOOO....      8 cols wide
..OOOOOOOO.#..
..............
```

### Scenario B: Area 35
Using corners `7,1` and `11,7`:
- Width: `|11 - 7| + 1 = 5`
- Height: `|7 - 1| + 1 = 7`
- Area: `5 * 7 = 35`
```
..............
.......OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
.......OOOOO..
..............
```

### Scenario C: The Max (Area 50)
Using corners `2,5` and `11,1`:
- Width: `|11 - 2| + 1 = 10`
- Height: `|5 - 1| + 1 = 5`
- Area: `10 * 5 = 50`

## Challenge
1. Parse the input list of coordinates.
2. Compare **every possible pair** of red tiles.
3. Calculate the rectangle area they would form if used as opposite corners.
4. Find the maximum area among all pairs.

## Output
- A single integer representing the largest area found.