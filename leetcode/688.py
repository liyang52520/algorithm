class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        # use dp
        # dp[step][row][col]代表走了step步时总可能位置数？
        dp = [[[100] * n for _ in range(n)] for _ in range(k + 1)]
        for step in range(k + 1):
            for c_row in range(n):
                for c_col in range(n):
                    if step == 0:
                        dp[step][c_row][c_col] = 1
                    else:
                        for x, y in ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)):
                            next_row = x + c_row
                            next_col = y + c_col
                            if 0 <= next_row < n and 0 <= next_col < n:
                                dp[step][c_row][c_col] += dp[step - 1][next_row][next_col] / 8

        return dp[k][row][column]


if __name__ == '__main__':
    print(Solution().knightProbability(3, 2, 0, 0))
