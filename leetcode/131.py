class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        results = []

        dp = [[False
               if i != j else True for j in range(len(s))]
              for i in range(len(s))]
        for step in range(2, len(s) + 1):
            for i in range(len(s) - step + 1):
                j = i + step - 1
                if s[i] == s[j]:
                    if step == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True

        def do_partition(start, pre):
            """

            Args:
                start:
                pre:

            Returns:

            """
            if start == len(s):
                results.append(pre)
            # search hui wen from start
            for i in range(start, len(s)):
                if dp[start][i]:
                    do_partition(i + 1, pre + [s[start:i + 1]])

        do_partition(0, [])
        return results

if __name__ == '__main__':
    print(Solution().partition("aab"))
