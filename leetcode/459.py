class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        next_arr = [-1] * len(s)
        j = -1
        for i in range(1, len(s)):
            while j >= 0 and s[i] != s[j + 1]:
                j = next_arr[j]
            if s[i] == s[j + 1]:
                j += 1
            next_arr[i] = j
        if next_arr[-1] == -1:
            return False
        part_len = len(s) - next_arr[-1] - 1
        return len(s) % part_len == 0


if __name__ == '__main__':
    print(Solution().repeatedSubstringPattern("abba"))
