class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(key=abs, reverse=True)

        for i in range(len(nums)):
            if k > 0 > nums[i]:
                nums[i] = -nums[i]
                k -= 1
            elif k == 0:
                break
        if k > 0:
            nums[-1] *= (-1) ** k
        return sum(nums)
