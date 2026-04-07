class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = min(len(s) for s in strs)
        common = ""
        for i in range(min_len):
            c = strs[0][i]
            for s in strs[1:]:
                if c != s[i]:
                    return common
            common += c
        return common
