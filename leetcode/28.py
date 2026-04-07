class Solution(object):
    def get_next(self, s):
        """

        Args:
            s:

        Returns:

        """
        # next[i] compute (most common front and tail - 1) in substr s_{0->i}, not contain first and last char
        next_list = [-1] * len(s)
        j = -1
        for i in range(1, len(s)):
            # s[j + 1] is 已经匹配的最长公共前后缀的长度
            while j >= 0 and s[i] != s[j + 1]:
                # 将j跳转到上一个s_{0->j}与s_{i-j->j}相同的地方，看可能不可能
                j = next_list[j]
            if s[i] == s[j + 1]:
                j += 1
            next_list[i] = j

        return next_list

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        # get next
        next_arr = self.get_next(needle)
        # find
        j = -1
        for i in range(len(haystack)):
            # not same, 寻找之前匹配的位置
            while j >= 0 and haystack[i] != needle[j + 1]:
                j = next_arr[j]
            # same
            if haystack[i] == needle[j + 1]:
                j += 1
            # find needle
            if j == len(needle) - 1:
                return i - j
        return -1


if __name__ == '__main__':
    a = "aabaabaafa"
    b = "aabaaf"
    print(a.index(b))
    print(Solution().strStr("aabaabaafa", "aabaaf"))
