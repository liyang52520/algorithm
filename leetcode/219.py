class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_idx_dict = {}
        for i, num in enumerate(nums):
            if num in num_idx_dict:
                if 0 < i - num_idx_dict[num] <= k:
                    return True
                else:
                    num_idx_dict[num] = i
            else:
                num_idx_dict[num] = i
        return False


if __name__ == '__main__':
    print(Solution().containsNearbyDuplicate([1, 0, 1, 1],
                                             1))
