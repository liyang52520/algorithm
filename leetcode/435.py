class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 1:
            return 1
        points.sort(key=lambda x: x[0])
        count = 0
        border = float("-inf")
        for start, end in points:
            if start >= border:
                count += 1
                border = end
            else:
                border = min(end, border)
        return count

    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        return len(intervals) - self.findMinArrowShots(intervals)