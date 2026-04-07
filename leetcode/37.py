class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows_occupy = [[False] * 9 for _ in range(9)]
        cols_occupy = [[False] * 9 for _ in range(9)]
        part_occupy = [[False] * 9 for _ in range(9)]

        # init
        for r, line in enumerate(board):
            for c, num in enumerate(line):
                if num != ".":
                    num = int(num)
                    rows_occupy[r][num - 1] = True
                    cols_occupy[c][num - 1] = True
                    part_occupy[(r // 3) * 3 + c // 3][num - 1] = True

        def do_solve(row, col):
            if row == 9:
                return True
            # if empty
            next_row = row + 1 if col == 8 else row
            next_col = 0 if col == 8 else col + 1
            if board[row][col] == ".":
                part = (row // 3) * 3 + col // 3
                for n in range(9):
                    if not rows_occupy[row][n] and not cols_occupy[col][n] and not part_occupy[part][n]:
                        # update
                        rows_occupy[row][n] = True
                        cols_occupy[col][n] = True
                        part_occupy[part][n] = True
                        board[row][col] = str(n + 1)
                        # next
                        if do_solve(next_row, next_col):
                            return True
                        # resume
                        board[row][col] = "."
                        rows_occupy[row][n] = False
                        cols_occupy[col][n] = False
                        part_occupy[part][n] = False
                return False
            else:
                return do_solve(next_row, next_col)

        do_solve(0, 0)


if __name__ == '__main__':
    a = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    b = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
         ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
         ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
         ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
         ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
         ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
         ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
         ["2", "8", "7", "4", ".", "9", "6", "3", "5"],
         ["3", "4", "5", "2", "8", "6", "1", ".", "9"]]

    Solution().solveSudoku(a)
    for i in a:
        print(i)
