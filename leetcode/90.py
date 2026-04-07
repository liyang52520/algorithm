class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        results = []

        def do_subsets(start, pre):
            """

            Args:
                start:
                pre:

            Returns:

            """
            results.append(pre)
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                do_subsets(i + 1, pre + [nums[i]])

        do_subsets(0, [])
        return results


if __name__ == '__main__':
    print(Solution().subsetsWithDup([1, 2, 2, 2]))
