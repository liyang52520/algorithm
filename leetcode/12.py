class Solution(object):
    def intToRoman(self, num):
        """
        :type remainder: int
        :rtype: str
        """
        res = ""
        count = 1
        while num > 0:
            remainder = num % 10
            if remainder <= 3:
                return res + "I" * remainder
            if remainder * count == 4:
                return res + "IV"
            if remainder * count == 9:
                return res + "IX"
            if remainder * count == 40:
                return res + "XL"
            if remainder * count == 90:
                return res + "XC"
            if remainder * count == 400:
                return res + "CD"
            if remainder * count == 900:
                return res + "CM"


            if remainder >= 1000:
                res += "M"
                remainder -= 1000
            elif remainder >= 500:
                res += "D"
                remainder -= 500
            elif remainder >= 100:
                res += "C"
                remainder -= 100
            elif remainder >= 50:
                res += "L"
                remainder -= 50
            elif remainder >= 10:
                res += "X"
                remainder -= 10
            elif remainder >= 5:
                res += "V"
                remainder -= 5

if __name__ == '__main__':
    print(Solution().intToRoman(1994))