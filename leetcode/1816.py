class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        count = 0
        for i, c in enumerate(s):
            if c == " ":
                count += 1
                if count == k:
                    return s[:i]
        return s
