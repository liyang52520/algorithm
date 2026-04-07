class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
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
                do_subsets(i + 1, pre + [nums[i]])

        do_subsets(0, [])
        return results


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
