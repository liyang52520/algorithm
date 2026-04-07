class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        def do_permute(start, pre):
            if start == len(nums):
                return results.append(pre)
            appeared = set()
            for i in range(start, len(nums)):
                if nums[i] in appeared:
                    continue
                nums[start], nums[i] = nums[i], nums[start]
                do_permute(start + 1, pre + [nums[start]])
                nums[start], nums[i] = nums[i], nums[start]
                appeared.add(nums[i])

        do_permute(0, [])
        return results


if __name__ == '__main__':
    print(Solution().permuteUnique([3, 3, 0, 3]))
