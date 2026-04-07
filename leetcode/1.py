class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        searched = {}
        for i, num in enumerate(nums):
            if target - num in searched:
                return [i, searched[target - num]]
            searched[num] = i
