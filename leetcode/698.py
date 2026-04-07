class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False

        dp = [0] * (nums_sum + 1)
        for num in nums:
            for c in range(nums_sum, -1, -1):
                if c >= num:
                    dp[c] = max(dp[c], dp[c - num] + num)
        for i in range(1, k):
            t = i * (nums_sum // k)
            if dp[t] != t:
                return False
        return True


if __name__ == '__main__':
    print(Solution().canPartitionKSubsets([2, 2, 2, 2, 3, 4, 5],
                                          4))
