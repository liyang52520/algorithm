class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        spans = {}
        for i, c in enumerate(s):
            if c in spans:
                spans[c][1] = i
            else:
                spans[c] = [i, i]
        spans = sorted(spans.values(), key=lambda x: x[0])
        border = -1
        pre_border = 0
        res = []
        all_len = 0
        # print(spans)
        for start, end in spans:
            if start >= border:
                if border == -1:
                    border = end
                    continue
                res.append(start - pre_border)
                all_len += res[-1]
                pre_border = start
                border = end
            else:
                border = max(end, border)
        res.append(len(s) - all_len)
        return res


if __name__ == '__main__':
    print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
