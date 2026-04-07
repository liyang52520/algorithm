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
            if start > border:
                count += 1
                border = end
            else:
                border = min(end, border)
        return count


if __name__ == '__main__':
    print(Solution().findMinArrowShots(
        [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]))
