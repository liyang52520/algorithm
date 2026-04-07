class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        results = []
        col_occupy = [False] * n

        def do_solve_n_queens(pre, pre_cols):
            # end condition
            row = len(pre)
            if row == n:
                results.append(pre)
            #
            for c, c_o in enumerate(col_occupy):
                if not c_o:
                    flag = True
                    for r, pre_c in enumerate(pre_cols):
                        if abs(row - r) == abs(pre_c - c):
                            flag = False
                            break
                    if flag:
                        col_occupy[c] = True
                        do_solve_n_queens(pre + ["." * c + "Q" + "." * (n - c - 1)], pre_cols + [c])
                        col_occupy[c] = False

        do_solve_n_queens([], [])
        return results


if __name__ == '__main__':
    print(Solution().solveNQueens(4))
