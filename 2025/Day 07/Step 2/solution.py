from functools import lru_cache

board = []
with open("input.txt", "r") as file:
    line = file.readline()
    while line != "":
        board.append([x for x in line.strip('\n')])
        line = file.readline()

START_BEAM_ROW = 0
start_beam_col = -1
STEP = 1

for i in range(len(board[0])):
    if board[0][i] == 'S':
        start_beam_col = i

@lru_cache
def beamPropagation(row, col):
    if(board[row][col] == '.'):
        if row + STEP < len(board):
            return beamPropagation(row + STEP, col)
        return 1
    elif board[row][col] == '^':
        left, right = 0, 0
        if col - STEP >= 0:
            left = beamPropagation(row, col - STEP)
        if col + STEP < len(board[row]):
            right = beamPropagation(row, col + STEP)
        return left + right
    else:
        return 0

beam_split = beamPropagation(START_BEAM_ROW + STEP, start_beam_col)

print("The solution is:", beam_split)