# Day 4: Printing Department - Part Two

## Problem Overview
The removal process is no longer static. Removing accessible paper rolls clears space, potentially reducing the neighbor count for remaining rolls and making them accessible in subsequent turns.

## The Iterative Process
1. **Scan:** Identify all paper rolls (`@`) that currently meet the access condition (fewer than 4 neighbors).
2. **Remove:** Mark all identified rolls for removal.
3. **Update:** Change those positions to empty space (`.`). They no longer count as neighbors for the remaining rolls.
4. **Repeat:** Scan the modified grid again.
5. **Stop:** Continue until a scan yields **0** new removable rolls.

### Access Rule (Unchanged)
A roll is removable if it has **< 4 neighbors** (`@`) in the 8 adjacent tiles.

## Example Scenario

### Simulation Trace
*Initial Grid contains many rolls.*

**Round 1:**
- Found **13** rolls with < 4 neighbors.
- Action: Remove them.

**Round 2:**
- Due to the holes created in Round 1, new rolls are exposed.
- Found **12** new rolls.
- Action: Remove them.

**Round 3:**
- More space opens up.
- Found **7** new rolls.

**Subsequent Rounds:**
- Round 4: **5** removed.
- Round 5: **2** removed.
- Round 6: **1** removed.
- Round 7: **1** removed.
- Round 8: **1** removed.
- Round 9: **1** removed.
- Round 10: **0** found. **STOP.**

### Final Calculation
Total rolls removed = `13 + 12 + 7 + 5 + 2 + 1 + 1 + 1 + 1` = **43**.

## Challenge
Run the simulation on your full puzzle input until the grid stabilizes (no more moves possible).

## Input
- The original grid configuration (same as Part One).

## Output
- A single integer representing the grand total of all paper rolls removed across all rounds.