from functools import lru_cache


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        # revert timepoints to minutes
        @lru_cache()
        def revert_time(time_point):
            """

            Args:
                time_point:

            Returns:

            """
            return 60 * int(time_point[:2]) + int(time_point[3:])

        time_points = list(map(revert_time, timePoints))
        time_points.sort()
        min_gap = float("inf")
        for i in range(1, len(time_points)):
            min_gap = min(min_gap, time_points[i] - time_points[i - 1])
        return min(min_gap, time_points[0] - time_points[-1] + 1440)


if __name__ == '__main__':
    print(Solution().findMinDifference(["00:00", "23:59"]))
