class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        dp = [[0, 0, 0, 0] for _ in range(len(prices))]
        # 0: 买入，买入需要不是freeze才能买
        # 1: 卖出后过了freeze持有的现金
        # 2: 刚卖出后持有的现金
        # 3: freeze，手上持有的现金等于前一天卖出的
        dp[0] = [-prices[0], 0, 0, 0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i], dp[i - 1][3] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
            dp[i][2] = dp[i - 1][0] + prices[i]
            dp[i][3] = dp[i - 1][2]
        return max(dp[-1][2], dp[-1][1], dp[-1][3])
