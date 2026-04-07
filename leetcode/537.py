class Solution(object):
    def split_num(self, num):
        """

        Args:
            num:

        Returns:

        """
        return tuple(map(int, num[:-1].split("+")))

    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        s_1, x_1 = self.split_num(num1)
        s_2, x_2 = self.split_num(num2)
        s = s_1 * s_2 - x_1 * x_2
        x = s_1 * x_2 + s_2 * x_1
        return "{}+{}i".format(s, x)


if __name__ == '__main__':
    print(Solution().complexNumberMultiply(num1 = "1+-1i", num2 = "1+-1i"))
