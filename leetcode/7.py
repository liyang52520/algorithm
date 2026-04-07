class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        flag = x < 0
        #
        x = abs(x)
        r = 0
        while x > 0:
            r = r * 10 + (x % 10)
            x = x // 10
        print(2**31)
        if r >= 2147483648:
            return 0

        return r if not flag else -r


if __name__ == '__main__':
    print(Solution().reverse(1563847412))
