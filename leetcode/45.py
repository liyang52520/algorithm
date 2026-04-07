class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        idx = 0
        cover = nums[0]
        count = 1
        while True:
            if cover >= len(nums) - 1:
                return count
            for i in range(idx + 1, cover + 1):
                if nums[i] + i > cover:
                    cover = nums[i] + i
                    idx = i
            count += 1


if __name__ == '__main__':
    print(Solution().jump([2, 3, 1, 1, 4]))
