class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []

        def do_combine_sum(t, pre):
            """"""
            if t < 0:
                return
            if t == 0:
                return results.append(pre)
            for num in candidates:
                if not len(pre) or num >= pre[-1]:
                    do_combine_sum(t - num, pre + [num])

        do_combine_sum(target, [])
        return results


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
