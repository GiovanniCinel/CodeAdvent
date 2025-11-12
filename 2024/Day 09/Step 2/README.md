# Day 9: Disk Fragmenter - Part Two

## Problem Overview
After the initial disk compaction, the amphipod proposes a new strategy for organizing the disk: moving whole files instead of individual blocks.

## New Compaction Rules
1. Move whole files to the leftmost span of free space that can accommodate them
2. Move files in order of *decreasing file ID number*
3. Start with the file with the highest file ID
4. If no suitable free space exists for a file, leave it in place

## Compaction Process Demonstration

### Initial Disk State
```
00...111...2...333.44.5555.6666.777.888899
```

### Compaction Steps
```
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
```

## Filesystem Checksum Calculation
- Same method as Part One
- Multiply each block's position by its file ID
- Sum these values
- Skip blocks with free space

### Checksum Example
In this demonstration, the checksum would be `2858`

## Challenge
Compact the amphipod's hard drive using the new whole-file movement method and calculate the resulting filesystem checksum.

## Input
- A string of digits representing file and free space lengths
- Alternating between file lengths and free space lengths

## Output
A single integer representing the filesystem checksum after compaction