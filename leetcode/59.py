class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]]
        # matrix for data
        matrix = [[0 for j in range(n)] for i in range(n)]
        matrix[0][0] = 1
        direct = 0
        fill_num = 2
        row = 0
        col = 0
        while fill_num <= n ** 2:
            if direct == 0:
                col += 1
                # right or down
                if col == n - 1:
                    direct = 3
                elif col < n - 1:
                    if not matrix[row][col + 1]:
                        direct = 0
                    else:
                        direct = 3

            elif direct == 1:
                col -= 1
                # left or up
                if col == 0:
                    direct = 2
                elif col > 0:
                    if not matrix[row][col - 1]:
                        direct = 1
                    else:
                        direct = 2
            elif direct == 2:
                row -= 1
                # up or right
                if not matrix[row - 1][col]:
                    direct = 2
                else:
                    direct = 0
            elif direct == 3:
                row += 1
                if row == n - 1:
                    direct = 1
                else:
                    if not matrix[row + 1][col]:
                        direct = 3
                    else:
                        direct = 1
            else:
                raise NotImplementedError
            matrix[row][col] = fill_num
            fill_num += 1
        return matrix


if __name__ == '__main__':
    res = Solution().generateMatrix(3)
    print("Result:")
    print(res)
