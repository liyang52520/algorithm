class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        max_res = float("-inf")
        for num in nums:
            res += num
            max_res = max(res,max_res)
            if res <= 0:
                res = 0
        return max_res