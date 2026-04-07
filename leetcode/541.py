class Solution(object):
    def reverse(self, s, left, right):
        """

        Args:
            s ():
            left ():
            right ():

        Returns:

        """
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        if len(s) < k:
            return "".join(s[::-1])
        if k <= len(s) < 2 * k:
            self.reverse(s, 0, k - 1)
            return "".join(s)
        idx = 0
        while idx < len(s) - k:
            self.reverse(s, idx, idx + k - 1)
            idx += 2 * k

        if idx < len(s):
            self.reverse(s, idx, len(s) - 1)

        return "".join(s)


if __name__ == '__main__':
    print(Solution().reverseStr(s="abcd", k=2))
