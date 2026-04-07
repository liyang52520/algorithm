class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        all_time = 0
        last_time = -1
        for t in timeSeries:
            if last_time >= t:
                all_time += duration - (last_time - t) - 1
            else:
                all_time += duration
            last_time = t + duration - 1
        return all_time


if __name__ == '__main__':
    print(Solution().findPoisonedDuration([1, 2, 3, 4, 5], 5))
