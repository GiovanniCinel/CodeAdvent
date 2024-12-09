# Day 9: Disk Fragmenter

## Problem Overview
While exploring a submarine facility, you encounter an amphipod struggling with disk fragmentation. Your task is to help compact the disk and calculate its filesystem checksum.

## Background Story
The Historians are exploring a submarine facility, each with a personal mini-submarine. An amphipod needs help compacting his computer's disk to create more contiguous free space.

## Input Format
- A string of digits representing file and free space lengths
- Alternating between file lengths and free space lengths
- Example: `2333133121414131402`

## Disk Representation
- Each digit represents the length of a file or free space block
- File ID is based on the original order of files
- Free space is represented by `.`

### Example Disk Representation
Input: `12345`
Representation: `0..111....22222`
- File 0: 1 block
- Free space: 2 blocks
- File 1: 3 blocks
- Free space: 4 blocks
- File 2: 5 blocks

## Compaction Process
1. Move file blocks from the end of the disk to the leftmost free space
2. Continue until no gaps remain between file blocks

### Compaction Example
```
0..111....22222
02.111....2222.
022111....222..
0221112...22...
02211122..2....
022111222......
```

## Filesystem Checksum Calculation
1. Multiply each block's position by its file ID
2. Sum these values
3. Skip blocks with free space

### Checksum Example
- Position 0, File ID 0: 0 * 0 = 0
- Position 1, File ID 0: 1 * 0 = 0
- Position 2, File ID 9: 2 * 9 = 18
- Position 3, File ID 9: 3 * 9 = 27
- Position 4, File ID 8: 4 * 8 = 32
- Total Checksum: 1928

## Challenge
Compact the amphipod's hard drive and calculate the resulting filesystem checksum.

## Input
Provide the disk map as a string of digits representing file and free space lengths.

## Output
A single integer representing the filesystem checksum after compaction.