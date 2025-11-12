# Day 2: Red-Nosed Reports

## Problem Overview

The Historians have been given some unusual data from the engineers, and they need your help to analyze it.

### Background

- The engineers have provided a series of "reports" containing levels of some kind
- Each report has 5 levels that are either all increasing, all decreasing, or a mix of increasing and decreasing
- The Historians need to determine which reports are "safe" and which are "unsafe"

### Puzzle Challenge

Analyze the unusual data from the engineers to determine how many reports are safe.

### Determining Safety

A report is considered safe if it meets one of the following criteria:

1. All levels are decreasing by 1 or 2
2. All levels are increasing

A report is considered unsafe if:

1. The levels have a mix of increasing and decreasing
2. The increase/decrease is more than 3

### Example Walkthrough

Given the following example data:

```
76421
12789
97621
33345 
86441
35679
```

Analyzing each report:
- 76421: Safe, all levels decreasing by 1 or 2
- 12789: Unsafe, all levels increasing
- 97621: Unsafe, mix of increasing and decreasing by more than 3
- 33345: Unsafe, mix of increasing and decreasing by more than 3
- 86441: Unsafe, mix of increasing and decreasing by more than 3 
- 35679: Safe, all levels decreasing by 1 or 2

In this example, 2 reports are safe and 4 reports are unsafe.

### Your Task

Analyze the unusual data provided by the engineers and determine how many reports are safe.

## Input

- A series of 5-level reports, each represented by a 5-digit number

## Output

- The number of safe reports
