class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []

        def do_restore(start, pre, count):
            """

            Args:
                start: start index of
                pre: pre part of id address
                count: count

            Returns:

            """
            # print(start, pre, count, results)
            if start == len(s):
                return

            if count == 3:
                if len(s) - start <= 3:
                    if start == len(s) - 1:
                        return results.append(pre + "." + s[-1])
                    if s[start] != "0" and int(s[start:]) <= 255:
                        return results.append(pre + "." + s[start:])
                else:
                    return

            # max 3
            for i in range(start, len(s)):
                if i - start >= 3:
                    break
                if i == start and s[start] == "0":
                    do_restore(i + 1, pre + ".0" if pre else "0", count + 1)
                    break
                if int(s[start:i + 1]) <= 255:
                    do_restore(i + 1, pre + "." + s[start:i + 1] if pre else s[start:i + 1], count + 1)

        do_restore(0, "", 0)

        return results


if __name__ == '__main__':
    print(Solution().restoreIpAddresses("0000"))
