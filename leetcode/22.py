class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ["()"]

        def do_generate(current, left, right):
            # invalid
            if left > right:
                return []

            if left == 0:
                return [current + ")" * right]
            if left == right and left == 1:
                return [current + "()"]

            add_left = []
            if left >= 1:
                add_left = do_generate(current + "(", left - 1, right)

            add_right = []
            if right >= 1:
                add_right = do_generate(current + ")", left, right - 1)

            return add_left + add_right

        return do_generate("", n, n)


if __name__ == '__main__':
    print(Solution().generateParenthesis(8))
