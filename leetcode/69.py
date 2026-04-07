class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        left, right = 1, x

        ans = 1
        while left <= right:
            mid = left + int((right - left) / 2)
            res = mid * mid
            if res <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


if __name__ == '__main__':
    print(Solution().mySqrt(3))
