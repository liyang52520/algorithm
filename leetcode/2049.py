class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        n = len(parents)
        # compute left and right tree for each node
        children = [[] for _ in range(len(parents))]
        for node, par in enumerate(parents):
            if par != -1:
                children[par].append(node)

        maxScore, cnt = 0, 0

        def dfs(node: int) -> int:
            score = 1
            size = n - 1
            for ch in children[node]:
                sz = dfs(ch)
                score *= sz
                size -= sz
            if node != 0:
                score *= size
            nonlocal maxScore, cnt
            if score == maxScore:
                cnt += 1
            elif score > maxScore:
                maxScore, cnt = score, 1
            return n - size

        dfs(0)
        return cnt


if __name__ == '__main__':
    print(Solution().countHighestScoreNodes([-1, 2, 0, 2, 0]))
