class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_cache = []

        # first k
        for num in nums[:k]:
            # 在他后面找到比他更大的，说明前面的无所谓，可以不存
            while len(num_cache) and num > num_cache[-1]:
                num_cache.pop(-1)
            num_cache.append(num)

        # 隐式的包含了一个东西，在前面的值一定比后面的值先出现
        res = [num_cache[0]]
        #
        idx = k
        while idx < len(nums):
            # delete out of window num
            if nums[idx - k] == num_cache[0]:
                num_cache.pop(0)
            # add new num
            num = nums[idx]
            while len(num_cache) and num > num_cache[-1]:
                num_cache.pop(-1)
            num_cache.append(num)
            res.append(num_cache[0])
            idx += 1

        return res


if __name__ == '__main__':
    print(Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
