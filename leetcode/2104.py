class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_min = [[-float("inf"), float("inf")] for _ in range(len(nums))]
        # dp[i] 代表 nums_{0->i} 的子数组范围和
        # dp[i] = dp[i - 1] 和 已 i 为结尾的所有子数组范围的和
        res = 0
        for i in range(0, len(nums)):
            for j, (max_val, min_val) in enumerate(max_min[:i + 1]):
                max_val = max(max_val, nums[i])
                min_val = min(min_val, nums[i])
                res += max_val - min_val
                max_min[j] = [max_val, min_val]
        return res


if __name__ == '__main__':
    print(Solution().subArrayRanges([4,-2,-3,4,1]))
