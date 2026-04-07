class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # sort the list
        nums.sort()
        n = len(nums)
        min_distance = float("inf")
        res = 0
        #
        for first_idx in range(0, n - 2):
            # filter repeat
            if first_idx > 0 and nums[first_idx] == nums[first_idx - 1]:
                continue
            for second_index in range(first_idx + 1, n - 1):
                # filter repeat too
                if second_index > first_idx + 1 and nums[second_index] == nums[second_index - 1]:
                    continue
                third_index = n - 1
                while third_index > second_index:
                    num = nums[first_idx] + nums[second_index] + nums[third_index]
                    distance = abs(num - target)
                    if distance < min_distance:
                        min_distance = distance
                        res = num
                    third_index -= 1
        return res
