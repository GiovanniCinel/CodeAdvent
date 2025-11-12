# Day 2: Red-Nosed Reports - Part Two

## Problem Continuation

The engineers are surprised by the low number of safe reports until they realize a problem: the Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be an unsafe report. 

## New Safety Rules

The same rules apply as before, except if removing a single level from an unsafe report makes it safe, the report is now considered safe.

## Additional Examples

More of the above example's reports are now safe:

- 76421: Safe without removing any level
- 12789: Unsafe, but safe by removing the first level
- 13245: Safe by removing the second level 
- 15679: Safe by removing the third level

## Challenge Update

Thanks to the Problem Dampener, 4 reports are now safe.

## Your Task

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?

## Input
- A series of 5-level reports, each represented by a 5-digit number

## Output
- The number of safe reports after applying the updated rules
