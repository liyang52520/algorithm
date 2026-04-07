class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        max_res = 1

        for step in range(2, len(s) + 1):
            for i in range(len(s) - step + 1):
                j = i + step - 1
                if s[i] == s[j]:
                    if step == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    if step == 2:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1], dp[i + 1][j - 1])
                max_res = max(max_res, dp[i][j])
        return max_res


if __name__ == '__main__':
    print(Solution().longestPalindromeSubseq("bbbab"))
