import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float("inf")] * (n+1)

        i = int(math.sqrt(n))
        nums = []
        while i > 0:
            nums.append(i ** 2)
        #     dp[i ** 2] = 1
            i -= 1
        dp[0] = 0
        # from big num to small one
        for num in nums[::-1]:
            for t in range(num, n + 1):
                dp[t] = min(dp[t - num] + 1, dp[t])
        return dp[n]


if __name__ == '__main__':
    print(Solution().numSquares(12))
