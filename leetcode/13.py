class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        last_num = 1001
        for i, c in enumerate(s):
            if nums[c] > last_num:
                res += nums[c] - 2 * nums[s[i - 1]]
            else:
                res += nums[c]
            last_num = nums[c]

        return res

if __name__ == '__main__':
    print(Solution().romanToInt("IX"))
