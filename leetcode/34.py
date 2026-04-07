class Solution(object):
    def binary_search(self, nums, target, equal=False):
        """
        find > or >=

        Args:
            nums ():
            target ():
            equal (bool):

        Returns:

        """
        left, right = 0, len(nums) - 1
        ans = len(nums)
        while left <= right:
            mid = left + int((right - left) / 2)
            if nums[mid] > target or (equal and nums[mid] >= target):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False) - 1
        if left <= right and nums[left] == target and nums[right] == target:
            return [left, right]
        return [-1, -1]


if __name__ == '__main__':
    print(Solution().searchRange([5, 5], 8))
