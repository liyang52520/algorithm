class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # sort candidates
        candidates = sorted(candidates)
        results = []

        def do_combination_sum(s, t, pre):
            """

            Args:
                s:
                t:
                pre:

            Returns:

            """
            if t < 0:
                return
            if t == 0:
                return results.append(pre)
            for i in range(s, len(candidates)):
                if i > s and candidates[i] == candidates[i - 1]:
                    continue
                do_combination_sum(i + 1, t - candidates[i], pre + [candidates[i]])

        do_combination_sum(0, target, [])
        return results


if __name__ == '__main__':
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
