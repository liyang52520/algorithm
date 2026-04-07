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

    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        s = s[::-1]
        s = list(s)
        self.reverse(s, 0, len(s) - n - 1)
        self.reverse(s, len(s) - n, len(s) - 1)
        return "".join(s)


if __name__ == '__main__':
    print(Solution().reverseLeftWords("abcdefg", 2))
