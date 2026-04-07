class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1, m2, idx = -1, -1, 0
        for i, num in enumerate(nums):
            if num > m1:
                m1, m2, idx = num, m1, i
            elif num > m2:
                m2 = num
        return idx if m1 >= m2 * 2 else -1


if __name__ == '__main__':
    print(Solution().dominantIndex([1, 2, 3, 4]))
