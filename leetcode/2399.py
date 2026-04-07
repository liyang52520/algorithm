from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i, c in enumerate(s):
            d = distance[ord(c) - ord("a")] + 1
            if i + d >= len(s) or s[i + d] != c:
                return False
            else:
                distance[ord(c) - ord("a")] = -1
        return True


if __name__ == '__main__':
    print(Solution().checkDistances("abaccb",
                                    [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
