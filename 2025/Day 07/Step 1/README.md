# Day 7: Laboratories

## Problem Overview
You are stuck in a teleporter lab with a malfunctioning tachyon
manifold. To repair it, you must simulate the flow of tachyon
beams through a grid of splitters to predict the total system activity.

## Manifold Mechanics

### Grid Elements
- `S`: **Source**. The starting point of the initial beam (top row).
- `.`: **Empty Space**. Beams pass through unchanged.
- `^`: **Splitter**. Interacts with beams.

### Beam Physics
1.  **Movement:** Beams always travel **downward** (increasing row index).
2.  **Splitting:**
    - When a vertical beam hits a splitter (`^`), it **stops**.
    - Two *new* beams are created immediately at the splitter's position.
    - **Left Branch:** Emerges from the column immediately to the left (`col - 1`).
    - **Right Branch:** Emerges from the column immediately to the right (`col + 1`).
3.  **Merging:**
    - If two different splitters send a beam into the *same* column (e.g.,
      a splitter at `col 4` sends right, and a splitter at `col 6` sends left,
      both targeting `col 5`), they form **one single beam**.
    - Beams do not "stack"; a column either has a beam or it doesn't.

## Example Scenario

### Initial State
The beam starts at `S` and moves down until it hits the first `^`.
```
.......S.......
.......|.......
.......^.......  <-- Hit!
...............
......^.^......
```

### The Split
The beam stops at the first `^`. Two new paths originate from the
left and right of that splitter.
```
.......S.......
.......|.......
......|^|......  <-- New beams start here
......|.|......
......^.^......  <-- Next targets
```

### The Merge Effect
Consider the next row where two splitters are close (`^.^`).
The left beam hits the left splitter; the right beam hits the right splitter.
- Left splitter sends to: Left & Center.
- Right splitter sends to: Center & Right.
- **Result:** The 'Center' receives input from both, but results in just **one** beam.
```
......|^|......
......|.|......
.....|^|^|.....  <-- 3 beams generated, not 4
```

### Final Flow
The process continues until beams exit the grid or hit no more splitters.
```
...|^|^|||^|...
...|.|.|||.|...
..|^|^|||^|^|..
..|.|.|||.|.|..
.|^|||^||.||^|.
.|.|||.||.||.|.
|^|^|^|^|^|||^|
```

## Scoring (The Challenge)
- You need to count the **Total Splits**.
- **Definition:** The number of times a beam successfully encounters a splitter (`^`).
- In the example above, the beam hits splitters a total of **21** times.

## Input
- A 2D grid of characters representing the manifold layout.

## Output
- A single integer representing the total count of beam splits.