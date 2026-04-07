class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        row_min = [min(row) for row in matrix]
        col_max = [max(col) for col in zip(*matrix)]
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if num == row_min[i] == col_max[j]:
                    res.append(num)
        return res


if __name__ == '__main__':
    print(Solution().luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
