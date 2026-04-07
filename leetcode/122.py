class Solution(object):
    def maxProfit_(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1, len(prices)):
            res += max(prices[i] - prices[i - 1], 0)
        return res

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # use dp
        # dp[0] 当前持有股票，还有的钱，dp[1] 当前手上没有股票，还有的钱
        dp = [0, 0]
        dp[0] = -prices[0]
        print(prices)
        print(dp)
        for i in range(1, len(prices)):
            dp[0], dp[1] = max(dp[0], dp[1] - prices[i]), max(dp[1], dp[0] + prices[i])
            print(dp)
        return dp[1]


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
