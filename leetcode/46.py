class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        def do_permute(start, pre):
            if start == len(nums):
                return results.append(pre)
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                do_permute(start + 1, pre + [nums[start]])
                nums[start], nums[i] = nums[i], nums[start]

        do_permute(0, [])

        return results


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
