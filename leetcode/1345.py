from collections import defaultdict, deque


class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        idxSameValue = defaultdict(list)
        for i, a in enumerate(arr):
            idxSameValue[a].append(i)
        visited = set()
        q = deque()
        q.append([0, 0])
        visited.add(0)
        while q:
            print(q)
            idx, step = q.popleft()
            if idx == len(arr) - 1:
                return step
            v = arr[idx]
            step += 1

            if idx + 1 < len(arr) and (idx + 1) not in visited:
                visited.add(idx + 1)
                q.append([idx + 1, step])
            if idx - 1 >= 0 and (idx - 1) not in visited:
                visited.add(idx - 1)
                q.append([idx - 1, step])

            for i in idxSameValue[v]:
                if i not in visited:
                    visited.add(i)
                    q.append([i, step])
            del idxSameValue[v]


if __name__ == '__main__':
    print(Solution().minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
