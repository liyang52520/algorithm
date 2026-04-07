class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) == 1:
            return t if t in s else ""

        if len(t) > len(s):
            return ""

        # count char in t
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        # find start idx
        start = 0
        while start < len(s):
            char = s[start]
            if char in t_count:
                break
            start += 1

        #
        end = start
        window_len = 0
        res_start = start
        res_len = len(s) + 1

        find_count = 0
        while end < len(s):
            end_char = s[end]
            if end_char in t_count:
                # find one char in window
                t_count[end_char] -= 1
                # become zero, one char has been found all
                if t_count[end_char] == 0:
                    find_count += 1
                # if find all chars in this window
                if find_count == len(t_count):
                    # update res
                    window_len = end - start + 1
                    # print(s[start:end + 1])
                    if window_len < res_len:
                        res_start, res_len = start, window_len
                    # search next window
                    # make window invalid
                    while start < len(s):
                        # find char
                        start_char = s[start]
                        if start_char in t_count:
                            # change t_count
                            t_count[start_char] += 1
                            # if window become invalid, it means contain start char is valid
                            if t_count[start_char] > 0:
                                # update res
                                window_len = end - start + 1
                                # print(s[start:end + 1])
                                if window_len < res_len:
                                    res_start, res_len = start, window_len
                                find_count -= 1
                                break
                        start += 1
                    # find next start
                    start += 1
                    while start < len(s):
                        if s[start] in t_count:
                            break
                        start += 1
            end += 1

        # not found any window
        if res_len == len(s) + 1:
            return ""
        return s[res_start:res_start + res_len]


if __name__ == '__main__':
    res = Solution().minWindow("aadafefeggeffaaaa", "aaa")
    print("\nResult:")
    print(res)
