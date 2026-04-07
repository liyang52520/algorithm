class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        if x < 10:
            return True
        if x % 10 == 0:
            return False

        right_part = 0
        while True:
            last_right_part = right_part
            right_part = right_part * 10 + x % 10
            x = x // 10
            if right_part >= x:
                return (last_right_part == x) or (right_part == x)


if __name__ == '__main__':
    print(Solution().isPalindrome(1211))
