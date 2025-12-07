# Day 7: Laboratories - Part Two

## Problem Overview
The manifold is actually a **Quantum Tachyon Manifold**. The previous understanding of "beams merging" was incorrect. According to the Many-Worlds Interpretation, every split creates distinct, parallel timelines.

## The Quantum Difference

### Part 1 (Classical Beam)
- Beams merge.
- If a beam arrives at a spot from the left, and another from the right, they become **1 beam**.
- **Logic:** `True OR True = True`

### Part 2 (Quantum Particle)
- Timelines branch.
- If a particle arrives at a spot from timeline A, and another arrives from timeline B, there are now **2 active timelines** at that spot.
- **Logic:** `1 + 1 = 2`

## Mechanics
- **Start:** 1 Particle (Timeline count: 1) at `S`.
- **Movement:** Downward.
- **Interaction with `.`:** The particle continues down. Timeline count remains unchanged.
- **Interaction with `^`:**
  - The universe splits.
  - The number of incoming timelines is passed to the **Left** neighbor (`col - 1`).
  - The *same* number of incoming timelines is passed to the **Right** neighbor (`col + 1`).

## Example Scenario

### Path visualization
A particle might take the "Always Left" path, or "Left then Right", etc.
Even if two paths end up at the same coordinate, they represent different histories.

**Example Grid (same as Part 1):**
- In Part 1, the total splits were 21.
- In Part 2, counting every possible unique path the particle could take through the splitters results in **40** distinct timelines.

### Massive Scaling
Because every splitter multiplies the number of paths by 2 (if paths don't merge), the number of timelines grows exponentially.
- *Note:* The puzzle answer provided (`16,937,871,060,075`) indicates the result will exceed standard 32-bit integer limits.

## Challenge
Re-calculate the flow through the manifold using quantum accumulation rules. Count the total number of timelines that successfully navigate the grid.

## Input
- The same 2D grid as Part One.

## Output
- A single (likely very large) integer representing the total number of active timelines.