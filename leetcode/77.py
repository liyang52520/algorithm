class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        results = []
        for i in range(1, n + 1):
            if n - i >= k - 1:
                results.extend(self.do_combine(i + 1, n, k - 1, [i]))
            else:
                break
        return results

    def do_combine(self, start, end, k, pre_result):
        """

        Args:
            start (int):
            end (int):
            k (int):
            pre_result (list):

        Returns:

        """
        # end of recursive
        if k == 0:
            return [pre_result]

        if k == 1:
            return [pre_result + [i] for i in range(start, end + 1)]

        if end - start + 1 == k:
            return [pre_result + list(range(start, end + 1))]

        new_results = []
        for i in range(start, end + 1):
            if end - i >= k - 1:
                new_results.extend(self.do_combine(i + 1, end, k - 1, pre_result + [i]))
            else:
                break
        return new_results


if __name__ == '__main__':
    print(Solution().combine(1, 1))
