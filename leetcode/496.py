class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: list
        :rtype: List[int]
        """
        res = []
        for n in nums1:
            idx = nums2.index(n)
            res.append(-1)
            for i in range(idx + 1, len(nums2)):
                if nums2[i] > n:
                    res[-1] = nums2[i]
                    break
        return res