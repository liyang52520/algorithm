class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        edge_set = set()
        for v, u in edges:
            if v in edge_set:
                return v
            else:
                edge_set.add(v)
            if u in edge_set:
                return u
            else:
                edge_set.add(u)