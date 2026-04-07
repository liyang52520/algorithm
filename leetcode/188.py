class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0:
            return 0
        if len(prices) == 0:
            return 0
        # 奇数买，偶数卖，0什么都不干
        dp_pre = [0] * (k * 2 + 1)
        dp_cur = [0] * (k * 2 + 1)
        # init dp_pre
        for i in range(0, k):
            dp_pre[i * 2 + 1] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(1, k * 2 + 1):
                if j % 2:
                    # in
                    dp_cur[j] = max(dp_pre[j], dp_pre[j - 1] - prices[i])
                else:
                    # out
                    dp_cur[j] = max(dp_pre[j], dp_pre[j - 1] + prices[i])
            dp_pre = dp_cur
        return dp_pre[-1]


if __name__ == '__main__':
    print(Solution().maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))
