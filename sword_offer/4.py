class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not (len(matrix) > 0 and len(matrix[0]) > 0):
            return False

        row, col = len(matrix), len(matrix[0])
        visited = [[False] * col for _ in range(row)]
        # dfs
        path_queue = [[0, col - 1]]
        while len(path_queue):
            c_row, c_col = path_queue.pop(0)
            visited[c_row][c_col] = True
            val = matrix[c_row][c_col]
            if val == target:
                return True
            if val > target:
                if c_col > 0 and not visited[c_row][c_col - 1]:
                    path_queue.append([c_row, c_col - 1])
                if c_row > 0 and not visited[c_row - 1][c_col - 1]:
                    path_queue.append([c_row - 1, c_col])
            else:
                if c_col < col - 1 and not visited[c_row][c_col + 1]:
                    path_queue.append([c_row, c_col + 1])
                if c_row < row - 1 and not visited[c_row + 1][c_col]:
                    path_queue.append([c_row + 1, c_col])

        return False


if __name__ == '__main__':
    print(Solution().findNumberIn2DArray([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 20))
