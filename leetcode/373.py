class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        data = [[i, j]
                for i in nums1[:k]
                for j in nums2[:k]]
        data.sort(key=lambda x: x[0] + x[1])
        return data[:k]


if __name__ == '__main__':
    print(Solution().kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=10))
    # print(Solution().kSmallestPairs(nums1=[1, 2], nums2=[3], k=3))
