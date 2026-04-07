class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if not nums or len(nums) < 4:
            return res

        nums.sort()
        n = len(nums)

        for first in range(n - 3):
            # repeat num
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # always gt
            if nums[first] + nums[first + 1] + nums[first + 2] + nums[first + 3] > target:
                break
            # always lt
            if nums[first] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
            for second in range(first + 1, n - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                third, fourth = second + 1, n - 1
                while third < fourth:
                    num_sum = nums[first] + nums[second] + nums[third] + nums[fourth]
                    if num_sum > target:
                        fourth -= 1
                    elif num_sum < target:
                        third += 1
                    else:
                        # add res
                        res.append([nums[first], nums[second], nums[third], nums[fourth]])
                        # update third and fourth
                        third += 1
                        fourth -= 1
                        while third < fourth and nums[third] == nums[third - 1]:
                            third += 1
                        while third < fourth and nums[fourth] == nums[fourth + 1]:
                            fourth -= 1
        return res
