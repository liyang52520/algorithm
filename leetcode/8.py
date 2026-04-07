import re


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = "".join(re.findall("^[-+]?\d+", s.strip()))
        n = int(s) if s else 0
        n = min(n, 2147483647)
        n = max(n,-2147483648)
        return n


if __name__ == '__main__':
    print(-2**31)
    print(Solution().myAtoi("words and 987"))
