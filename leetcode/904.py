class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        if len(fruits) <= 1:
            return len(fruits)
        # init
        start, end = 0, 1
        max_res = 1
        got = [-1, -1]
        got[0] = fruits[0]
        last_continue = 1

        while end < len(fruits):
            max_res += 1
            end += 1
            if fruits[end - 1] not in got:
                got[1] = fruits[end - 1]
                break

        # just one type fruit
        if got[1] == -1:
            return len(fruits)

        last_fruit = got[1]

        res = max_res
        while end < len(fruits):
            if fruits[end] not in got:
                max_res = max(res, max_res)
                res = last_continue + 1
                idx = int(not got.index(last_fruit))
                got[idx] = fruits[end]
                last_fruit = fruits[end]
                last_continue = 1
            else:
                if last_fruit == fruits[end]:
                    last_continue += 1
                else:
                    last_fruit = fruits[end]
                    last_continue = 1
                res += 1
            end += 1
        return max(max_res, res)


if __name__ == '__main__':
    print(Solution().totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3]))
