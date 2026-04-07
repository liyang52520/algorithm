class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        left, right = 1, num

        while left <= right:
            mid = left + int((right - left) / 2)
            res = mid * mid
            if res == num:
                return True
            if res < num:
                left = mid + 1
            else:
                right = mid - 1
        return False