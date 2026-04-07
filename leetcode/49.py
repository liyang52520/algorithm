from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        template = "abcdefghijklmnopqrstuvwxyz"
        res_dict = {}
        res = []
        for word in strs:
            counter = defaultdict(int)
            for c in word:
                counter[c] += 1
            temp_key = ""
            for c in template:
                temp_key += c * counter[c]
            idx = res_dict.setdefault(temp_key, len(res_dict))
            if idx >= len(res):
                res.append([word])
            else:
                res[idx].append(word)
        return res


if __name__ == '__main__':
    print(Solution().groupAnagrams([""]))
