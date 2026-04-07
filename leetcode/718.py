class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dp = [[0
               for j in range(len(nums1))]
              for i in range(len(nums2))]

        max_step = 0
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums2[i] == nums1[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    max_step = max(dp[i][j], max_step)
                else:
                    dp[i][j] = 0
        return max_step


if __name__ == '__main__':
    print(Solution().findLength([1, 2, 3, 2, 8],
                                [5, 6, 1, 4, 7]))
