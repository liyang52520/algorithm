class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        digit_letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        for c in digit_letters[int(digits[0])]:
            res.append(c)

        for digit in digits[1:]:
            new_res = []
            for c in digit_letters[int(digit)]:
                for r in res:
                    new_res.append(r + c)
            res = new_res
        return res


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
