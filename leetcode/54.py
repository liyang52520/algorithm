class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])

        if m == 1:
            return matrix[0]

        # use loop
        num = 0
        res = [0] * (m * n)
        left, right, up, down = 0, n - 1, 0, m - 1
        while num < m * n:
            for i in range(left, right + 1):
                res[num] = matrix[up][i]
                num += 1
            up += 1
            for i in range(up, down + 1):
                res[num] = matrix[i][right]
                num += 1
            right -= 1
            if left <= right and up <= down:
                for i in range(right, left - 1, -1):
                    res[num] = matrix[down][i]
                    num += 1
                down -= 1
                for i in range(down, up - 1, -1):
                    res[num] = matrix[i][left]
                    num += 1
                left += 1
        return res


if __name__ == '__main__':
    print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
