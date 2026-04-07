import math


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        y_sum = 1
        y = 2
        max_y = num
        while y < max_y and y < math.sqrt(num):
            if num % y == 0:
                max_y = num / y
                y_sum += y + max_y

            y += 1
        return y_sum == num

if __name__ == '__main__':
    print(Solution().checkPerfectNumber(1))
