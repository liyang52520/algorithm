class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        chars = set(list("qwertyuiopasdfghjklzxcvbnm"))
        for i, c in enumerate(s):
            if c == "?":
                # need to modify
                for n in chars:
                    if i > 0 and s[i-1] == n:
                        continue
                    if i < len(s) - 1 and s[i + 1] == n:
                        continue
                    s[i] = n
                    break
        return "".join(s)
