class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        batch_size = numRows * 2 - 2
        res = ""
        for row in range(numRows):
            if batch_size - row * 2 == 0 or row == 0:
                # first or last
                for c in s[row::batch_size]:
                    res += c
            else:
                step = batch_size - 2 * row
                for i in range(row, len(s), batch_size):
                    res += s[i]
                    if i + step < len(s):
                        res += s[i + step]
        return res


if __name__ == '__main__':
    print(Solution().convert("A", 1))
