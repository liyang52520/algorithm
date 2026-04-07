class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        dp = [-prices[0], 0]
        for i in range(1, len(prices)):
            dp[0], dp[1] = max(-prices[i], dp[0]), max(dp[1], dp[0] + prices[i])
        return dp[1]