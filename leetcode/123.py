class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [0, -prices[0], 0, -prices[0], 0]
        print(dp)
        for i in range(1, len(prices)):
            # dp[1] 更新的是什么时候第一次买更便宜
            # 
            dp[1], dp[2], dp[3], dp[4] = max(dp[0] - prices[i], dp[1]), max(dp[2], dp[1] + prices[i]), max(dp[3],
                                                                                                           dp[2] -
                                                                                                           prices[
                                                                                                               i]), max(
                dp[4], dp[3] + prices[i])
            print(dp)
        return dp[4]


if __name__ == '__main__':
    print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
