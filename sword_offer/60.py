class Solution(object):
    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        s = list(S)
        results = []

        def do_permute(start):
            """

            Args:
                start:

            Returns:

            """
            if start == len(s) - 1:
                results.append("".join(s))
                return
            appeared = set()
            for idx in range(start, len(s)):
                if s[idx] in appeared:
                    continue
                s[start], s[idx] = s[idx], s[start]
                do_permute(start + 1)
                s[start], s[idx] = s[idx], s[start]
                appeared.add(s[idx])

        do_permute(0)

        return results