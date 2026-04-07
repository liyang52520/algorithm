class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        results = []
        tickets_used = [False] * len(tickets)
        used_count = 0

        def do_find(start, pre):
            """"""
            # end condition
            nonlocal used_count
            if used_count == len(tickets_used):
                results.append(pre + [start])
                return True

            # choose max
            ends = []
            for i, t_u in enumerate(tickets_used):
                if not t_u and tickets[i][0] == start:
                    ends.append((tickets[i][1], i))
            ends.sort(key=lambda x: x[0], reverse=False)
            for end, end_idx in ends:
                # next
                tickets_used[end_idx] = True
                used_count += 1
                if do_find(end, pre + [start]):
                    return True
                tickets_used[end_idx] = False
                used_count -= 1

        do_find("JFK", [])
        return results[0]


if __name__ == '__main__':
    print(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
