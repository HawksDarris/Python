'''
understanding:
    we have index 0 through index 8
        each having index 0 through index 8

    that's 81 cells.

    a cell can be 1-9, but it cannot match a number in its row or column
    It also cannot match a number in its 3x3 grid (but I think that is implied by the row and column thing)

Plan:

    1. if 0, iterate
    2. loop through puzzle[row][col], every number.
    3. if row or column match, iterate
    4. loop through 3x3 grid of puzzle[row][col]
    5. if number matches, iterate
    6. if it doesn't match, set puzzle[row][col] = num
    7. Check if it's solved with that changed value recursively
'''


puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

test = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
           [10, 11, 12, 13, 14, 15, 16, 17, 18],
           [19, 20, 21, 22, 23, 24, 25, 26, 27],
           [28, 29, 30, 31, 32, 33, 34, 35, 36],
           [37, 38, 39, 40, 41, 42, 43, 44, 45],
           [46, 47, 48, 49, 50, 51, 52, 53, 54],
           [55, 56, 57, 58, 59, 60, 61, 62, 63],
           [64, 65, 66, 67, 68, 69, 70, 71, 72],
           [73, 74, 75, 76, 77, 78, 79, 80, 81]]

original_lists = [
    [1, 0, 3, 0, 5, 0, 7, 0, 9],
    [2, 0, 4, 0, 6, 0, 8, 0, 10],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 1, 0, 2, 0, 3, 0, 4, 0],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0]
]

challenge = [
        [0,9,0, 0,0,0, 0,4,0],
        [0,0,0, 5,4,0, 0,3,0],
        [6,2,0, 0,0,9, 0,0,0],
        [0,0,0, 0,0,0, 3,0,0],
        [8,0,0, 0,0,0, 0,0,0],
        [0,0,0, 0,7,0, 6,0,8],
        [0,6,0, 0,0,3, 0,0,9],
        [3,0,8, 0,0,5, 4,0,0],
        [2,4,0, 0,0,6, 7,0,0]
        ]

def sudoku(puzzle):
    def is_candidate(puzzle, row, col, num):
        # check row for repeats
        if num in puzzle[row]:
            return False

        # check index for repeats
        for i in range(9):
            if puzzle[i][col] == num:
                return False

        # check 3x3 for repeats
        minigrid_row = (row // 3) * 3
        minigrid_col = (col // 3) * 3
        for i in range(minigrid_row, minigrid_row + 3): # get three rows
            for j in range(minigrid_col, minigrid_col + 3): # get three columns
                if puzzle[i][j] == num: # False if the number matches, True if the loop finishes without returning False.
                    return False
        return True

    def solved(puzzle):
        for row in range(9):
            for col in range(9):
                if not isinstance(puzzle[row][col], int) or puzzle[row][col] > 9: # if it is not an integer or an invalid number, the puzzle is unsolvable, return False
                    return False
                if puzzle[row][col] == 0:
                    for num in range(1, 10):
                        if is_candidate(puzzle, row, col, num):
                            puzzle[row][col] = num # change number
                            if solved(puzzle): # check if that value works
                                return True # if so, the puzzle is solved
                            puzzle[row][col] = 0  # back to blank for this cell if not, go to next number.
                    return False
        return True

    if solved(puzzle):
        return puzzle
    else:
        return 'No solution'


print(sudoku(challenge))
