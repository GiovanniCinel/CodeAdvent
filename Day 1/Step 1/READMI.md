# Day 1: Historian Hysteria

## Problem Overview

The Chief Historian has gone missing, and you're tasked with helping the Senior Historians locate him by solving a series of puzzles to collect stars.

### Background

- The Historians are trying to create a complete list of historically significant locations
- Each location is identified by a unique location ID
- The Historians have two lists of location IDs that seem different

## Part One: List Distance Calculation

### Puzzle Challenge

Calculate the total distance between two lists of location IDs by pairing and measuring differences.

### Pairing Rules

1. Pair up numbers from the left and right lists
2. Pair smallest with smallest, second-smallest with second-smallest, and so on
3. Calculate the absolute difference between paired numbers

### Example Walkthrough

Given lists:
```
Left List:  3 4 2 1 3 3
Right List: 4 3 5 3 9 3
```

Pairing and Distance Calculation:
- Smallest left (1) paired with smallest right (3): Distance = |1 - 3| = 2
- Second-smallest left (2) paired with second-smallest right (3): Distance = |2 - 3| = 1
- Next pair (3 and 3): Distance = |3 - 3| = 0
- Next pair (3 and 4): Distance = |3 - 4| = 1
- Next pair (3 and 5): Distance = |3 - 5| = 2
- Largest left (4) paired with largest right (9): Distance = |4 - 9| = 5

**Total Distance: 2 + 1 + 0 + 1 + 2 + 5 = 11**

### Challenge Goal

Calculate the total distance between your specific left and right lists of location IDs.

## Input

- Two lists of integers representing location IDs

## Output

- A single integer representing the total distance between the lists

## Puzzle Objectives

- Collect stars by solving puzzles
- Unlock the second puzzle by completing the first
- Help the Historians find the Chief Historian's potential locations
