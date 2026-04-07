class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        for i in range(1, 11 - k):
            results.extend(self.do_combine_sum(i + 1, k - 1, n - i, [i]))
        return results

    def do_combine_sum(self, start, k, n, pre):
        """

        Args:
            start:
            k:
            n:
            pre (list):

        Returns:

        """
        if n < 0:
            return []
        if k == 0:
            return [pre] if n == 0 else []
        results = []
        for i in range(start, 11 - k):
            results.extend(self.do_combine_sum(i + 1, k - 1, n - i, pre + [i]))
        return results


if __name__ == '__main__':
    print(Solution().combinationSum3(3, 3))
