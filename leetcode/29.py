class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0

        flag = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor > dividend:
            return 0

        if divisor == dividend:
            return -(-1) ** flag

        # assure 正的 且 dividend > divisor
        res = divisor
        pre_res = divisor
        m = 0
        while res < dividend:
            pre_res = res
            res += res
            m += 1
        if res == dividend:
            res = -(-1) ** flag * (2 ** m)
            if res == 2147483648:
                return 2147483647
            return res

        res = -(-1) ** flag * (2 ** (m - 1) + self.divide(dividend - pre_res, divisor))
        if res== 2147483648:
            return 2147483647
        return res

if __name__ == '__main__':
    print(Solution().divide(-2147483648, -1))
