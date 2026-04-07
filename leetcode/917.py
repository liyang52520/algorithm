class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = [""] * len(s)
        left, right = 0, len(s) - 1
        while left <= right:
            while left <= right and not str.isalpha(s[left]):
                res[left] = s[left]
                left += 1
            while right >= left and not str.isalpha(s[right]):
                res[right] = s[right]
                right -= 1
            if left <= right:
                res[left], res[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(res)


if __name__ == '__main__':
    print(Solution().reverseOnlyLetters(s="Test1ng-Leet=code-Q!"))
