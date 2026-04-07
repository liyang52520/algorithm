class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)

        max_len = 0
        left = 0
        right = 0
        appeared = {}
        while left < len(s):
            while right < len(s):
                if s[right] not in appeared or appeared[s[right]] < left:
                    appeared[s[right]] = right
                else:
                    break
                right += 1
            if right == len(s):
                return max(max_len, right - left)
            else:
                max_len = max(max_len, right - left)
                left = appeared[s[right]] + 1
        return max_len


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("dvdf"))
