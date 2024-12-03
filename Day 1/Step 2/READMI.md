# Day 1: Location ID Similarity Scoring

## Part Two: Decoding the Historians' Lists

### Problem Description

The Historians have two lists of numbers that seem different at first glance. Your task is to calculate a unique "similarity score" by comparing these lists.

### Puzzle Rules

- Take the first list (left list) as your primary reference
- For each number in the left list:
  - Count how many times it appears in the right list
  - Multiply the number by its occurrence count
  - Add this value to the total similarity score

### Example Walkthrough

Given lists: 
3   4  
4   3  
2   5  
1   3  
3   9  
3   3  `

Similarity score calculation:
1. First number (3):
   - Appears 3 times in right list
   - Score increases by: 3 * 3 = 9

2. Second number (4):
   - Appears 1 time in right list
   - Score increases by: 4 * 1 = 4

3. Third number (2):
   - Does not appear in right list
   - Score increases by: 2 * 0 = 0

4. Fourth number (1):
   - Does not appear in right list
   - Score increases by: 1 * 0 = 0

5. Fifth number (3):
   - Appears 3 times in right list
   - Score increases by: 3 * 3 = 9

6. Last number (3):
   - Appears 3 times in right list
   - Score increases by: 3 * 3 = 9

**Total Similarity Score: 31**

### Challenge

Calculate the similarity score for your specific left and right lists.

## Input

- Two lists of numbers

## Output

- A single integer representing the total similarity score
