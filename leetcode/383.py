from collections import defaultdict


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r_counter = defaultdict(int)
        for c in ransomNote:
            r_counter[c] += 1

        find_count = 0
        for c in magazine:
            if c in r_counter:
                r_counter[c] -= 1
                if r_counter[c] == 0:
                    find_count += 1

        return find_count >= len(r_counter)


if __name__ == '__main__':
    print(Solution().canConstruct("aa", "aab"))
