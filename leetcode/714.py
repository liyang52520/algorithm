class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # 0 手上没股票有的最多现金，1 手上有股票有的最多现金
        dp = [0, -prices[0]]

        for i in range(1, len(prices)):
            dp[0], dp[1] = max(dp[0], dp[1] + prices[i] - fee), max(dp[1], dp[0] - prices[i])
        return dp[0]


if __name__ == '__main__':
    print(Solution().maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
