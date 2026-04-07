class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        def extend_s(left, right):
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    left += 1
                    right -= 1
                    break
            if left < 0 or right >= len(s):
                left += 1
                right -= 1
            return left, right

        max_start, max_end = 1, 0
        for i in range(len(s) - 1):
            s_1, e_1 = extend_s(i, i)
            s_2, e_2 = extend_s(i, i + 1)
            if e_1 - s_1 > max_end - max_start:
                max_start, max_end = s_1, e_1
            if e_2 - s_2 > max_end - max_start:
                max_start, max_end = s_2, e_2
        return s[max_start:max_end + 1]


if __name__ == '__main__':
    print(Solution().longestPalindrome("a"))
