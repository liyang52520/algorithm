class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """

        Args:
            nums1:
            nums2:

        Returns:

        """

        def get_kth(k):
            """

            Args:
                k:

            Returns:

            """
            part_1 = min(len_1, k // 2)
            part_2 = min(len_2, k // 2)

        len_1, len_2 = len(nums1), len(nums2)
        len_all = len_1 + len_2

        if len_all % 2 == 1:
            return get_kth((len_all + 1) // 2 - 1)
        else:
            return (get_kth(len_all // 2 - 1) + get_kth(len_all // 2)) / 2
