import re


class Solution(object):
    def reverse_word(self, s, left, right):
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

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = re.sub(" +", " ", s.strip())[::-1]
        # reverse each word
        left, right = 0, 0
        s = list(s)
        while right < len(s):
            while right < len(s):
                if s[right] == " ":
                    break
                right += 1
            self.reverse_word(s, left, right - 1)
            left = right + 1
            right = left
        return "".join(s)


if __name__ == '__main__':
    print(Solution().reverseWords("  Bob    Loves  Alice   "))
