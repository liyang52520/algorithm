class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for a in range(amount + 1):
                if a - coin >= 0:
                    dp[a] += dp[a - coin]
            print(dp)
        return dp[amount]


if __name__ == '__main__':
    print(Solution().change(5, [1, 2, 5]))
