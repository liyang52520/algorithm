class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        def do_find(start, pre):
            if len(pre) >= 2:
                results.append(pre)
            if start == len(nums):
                return
            appeared = set()
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                if nums[i] in appeared:
                    continue
                if not len(pre) or nums[i] >= pre[-1]:
                    do_find(i + 1, pre + [nums[i]])
                appeared.add(nums[i])

        do_find(0, [])
        return results


if __name__ == '__main__':
    print(Solution().findSubsequences([1, 2, 3, 1, 2]))
