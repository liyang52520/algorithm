class Solution(object):
    def maxSubArray_(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float("-inf")
        num_sum = 0
        for num in nums:
            num_sum += num
            res = max(num_sum, res)
            if num_sum <= 0:
                num_sum = 0
        return res

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])  # 状态转移公式
            result = max(result, dp[i])  # result 保存dp[i]的最大值
        return result


if __name__ == '__main__':
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
