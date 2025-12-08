# Day 8: Playground

## Problem Overview
You have teleported to a vast underground playground. To assist with
Christmas decorations, you must simulate the electrical wiring of
floating junction boxes.

## Core Mechanics
- **Input:** A list of 3D coordinates (`X,Y,Z`), one per line.
- **Object:** Each coordinate represents a junction box.
- **Goal:** Connect boxes to form electrical circuits.

## Connection Rules
1.  **Distance Metric:** Connections are based on 'straight-line distance'
    (Euclidean distance in 3D space).
2.  **Priority:** You must prioritize connecting the pairs that are closest
    together first.
3.  **Circuit Formation:**
    - Connecting two boxes merges them into the same circuit.
    - If you connect Box A and Box B, and Box B is already connected to Box C,
      then A, B, and C all become part of the same circuit.
4.  **Redundancy:**
    - If the next shortest pair of boxes is *already* in the same circuit
      (connected indirectly), the connection is made but effectively
      "nothing happens" (the circuit size doesn't change).
    - **Crucial:** This still counts as one of your allowed connections.

## Example Scenario
Consider a small list of 20 boxes. You make the **10 shortest connections**.

- **Step 1:** Connect closest pair. (Result: 1 circuit of size 2).
- **Step 2:** Connect next closest pair. (Result: 1 circuit of size 3).
- ...
- **Step X:** Connect a pair that is *already* in the same group. (No change).

### Example Outcome
After the 10 shortest connections are processed, the circuits look like this:
- One circuit of size **5**
- One circuit of size **4**
- Two circuits of size **2**
- Seven circuits of size **1** (isolated boxes)

**Scoring:** Multiply the sizes of the three largest circuits.
Calculation: `5 * 4 * 2 = 40`

## Challenge
1.  Parse the full input list of junction boxes.
2.  Calculate distances between *all possible pairs*.
3.  Select exactly the **1000 pairs** with the shortest distances.
4.  Process these connections in order to merge the boxes into circuits.
5.  Identify the **three largest circuits** resulting from this process.

## Output
- Multiply the sizes of the three largest circuits together.
- Return the resulting integer.