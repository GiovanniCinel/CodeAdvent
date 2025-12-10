# Day 9: Movie Theater - Part Two

## Problem Overview
The Elves clarify a crucial rule: you can't just pick any two red tiles.
Your rectangle must be built strictly on safe ground.

## New Terrain Definitions
1.  **The Loop (Perimeter):**
    - The input list forms a continuous loop.
    - Every red tile connects to the next one in the list via a straight
      line of **Green** tiles.
    - The list wraps around: the last tile connects back to the first.
    - *Hint:* Adjacent list items always share an X or Y coordinate
      (Manhattan geometry).

2.  **The Interior:**
    - All tiles **inside** this closed loop are also **Green**.

3.  **Validity Rule:**
    - The rectangle defined by two red corners is valid ONLY IF
      every single tile within that rectangle is either Red or Green.
    - In geometric terms: The rectangle must be completely contained
      within (or on the boundary of) the polygon defined by the input list.

## Example Scenario

### Visualizing the Zone
(`X` = Green, `#` = Red)
```
..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
```

### Valid Rectangle (Area 15)
Between `7,3` and `11,1`. It stays entirely in the green/red area.
```
..............
.......OOOOO..
.......OOOOO..
..#XXXXOOOOO..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
```

### Valid Rectangle (Area 24 - MAX)
Between `9,5` and `2,3`.
```
..............
.......#XXX#..
.......XXXXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
.........XXX..
.........#X#..
..............
```

## Challenge
1. Re-scan all pairs of Red tiles.
2. For each pair, form a candidate rectangle.
3. **Check Validity:** Does this rectangle overlap with any empty space (`.`)?
   - If it contains ANY non-green/non-red tile, it is invalid.
4. Find the largest area among only the **valid** rectangles.

## Output
- A single integer representing the maximum valid area.