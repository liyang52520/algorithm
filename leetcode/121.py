class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[0]代表第一次买入后手上的金额，dp[1]代表第一次卖出后，手上的金额
        dp = [-prices[0], 0]
        for price in prices[1:]:
            dp[0], dp[1] = max(dp[0], -price), max(dp[1], dp[0] + price)
        return dp[1]
