class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for part in range(1, len(s) + 1):
            for word in wordDict:
                if part >= len(word) and s[part - len(word):part] == word:
                    dp[part] = dp[part - len(word)] or dp[part]

        return dp[len(s)]


if __name__ == '__main__':
    print(Solution().wordBreak("dogs",
                               ["dog", "s", "gs"]
                               ))
