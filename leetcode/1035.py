class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # dp[i][j] 代表了 子串 i, j 的最长公共子序列，并不强制以其结尾
        dp = [[0] * len(nums2) for _ in range(len(nums1))]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if i == 0 or j == 0:
                    if j != 0:
                        if nums1[i] == nums2[j]:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = dp[i][j - 1]
                    else:
                        if nums1[i] == nums2[j]:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = dp[i - 1][j]
                else:
                    if nums1[i] == nums2[j]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                # print(f"{i}\t{j}\tdp: {dp[i][j]}")
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().maxUncrossedLines([1, 2, 2, 2, 1, 2],
                                       [1]))
