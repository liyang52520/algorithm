class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_idx = len(s) - 1
        s_delete_count = 0
        t_idx = len(t) - 1
        t_delete_count = 0
        while s_idx >= 0 and t_idx >= 0:
            if s[s_idx] == "#":
                s_delete_count += 1
                s_idx -= 1
            else:
                if s_delete_count != 0:
                    s_delete_count -= 1
                    s_idx -= 1
                else:
                    if t_delete_count == 0:
                        if s[s_idx] != t[t_idx] and t[t_idx] != "#":
                            return False
                        if s[s_idx] == t[t_idx]:
                            s_idx -= 1
                            t_idx -= 1
                            continue

            if t[t_idx] == "#":
                t_delete_count += 1
                t_idx -= 1
            else:
                if t_delete_count != 0:
                    t_delete_count -= 1
                    t_idx -= 1
                else:
                    if s_delete_count == 0:
                        if s[s_idx] != t[t_idx] and s[s_idx] != "#":
                            return False
                        if s[s_idx] == t[t_idx]:
                            s_idx -= 1
                            t_idx -= 1
                            continue
        if s_idx < 0 and t_idx < 0:
            return True
        # assert t_idx < 0:
        if s_idx < 0:
            t_idx, s_idx = s_idx, t_idx
            t_delete_count, s_delete_count = s_delete_count, t_delete_count
            t, s = s, t

        if s_idx == 0 and s[0] != "#" and s_delete_count <= 0:
            return False
        while s_idx >= 0:
            if s[s_idx] == "#":
                s_delete_count += 1
            else:
                if s_delete_count > 0:
                    s_delete_count -= 1
                else:
                    return False
            s_idx -= 1
        return s_delete_count >= 0


if __name__ == '__main__':
    print(Solution().backspaceCompare("j##yc##b",
                                      "j##yc##bs#srqpf#zantto###########i#mwb"))
