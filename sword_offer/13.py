class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 1

        nums = [0] * max(m, n)
        for i in range(len(nums)):
            nums[i] = self.split_num(i)

        arrived = [[False] * n for _ in range(m)]

        count = 0

        def do_move(row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return
            if arrived[row][col]:
                return
            if nums[row] + nums[col] > k:
                return
            nonlocal count
            count += 1
            arrived[row][col] = True
            do_move(row - 1, col)
            do_move(row + 1, col)
            do_move(row, col - 1)
            do_move(row, col + 1)

        do_move(0, 0)
        return count

    def split_num(self, num):
        """

        Args:
            num:

        Returns:

        """
        num_sum = 0
        while num:
            num_sum += num % 10
            num //= 10
        return num_sum


if __name__ == '__main__':
    print(Solution().movingCount(7, 2, 3))
