import re


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return re.search(f'^{p}$', s) is not None


if __name__ == '__main__':
    print(Solution().isMatch("aa", "a*"))
