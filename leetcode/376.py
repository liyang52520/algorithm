class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre, cur, res = 0, 0, 1
        for i in range(len(nums) - 1):
            cur = nums[i + 1] - nums[i]
            if cur * pre <= 0 and cur != 0:
                res += 1
                pre = cur
        return res


if __name__ == '__main__':
    print(Solution().wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
