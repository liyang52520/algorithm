from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_counter = defaultdict(int)
        for c in s:
            s_counter[c] += 1

        zero_count = 0
        for c in t:
            if c not in s_counter:
                return False
            else:
                s_counter[c] -= 1
                if s_counter[c] == 0:
                    zero_count += 1
                elif s_counter[c] < 0:
                    return False
        return zero_count == len(s_counter)
