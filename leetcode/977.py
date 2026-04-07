class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums[0] >= 0:
            for i, num in enumerate(nums):
                nums[i] = num ** 2
            return nums

        if nums[-1] <= 0:
            for i, num in enumerate(nums):
                nums[i] = num ** 2
            nums.reverse()
            return nums

        # read num from negative to zero
        negative_part = []
        apart_idx = -1
        for i, num in enumerate(nums):
            if num > 0:
                # get apart idx
                if apart_idx == -1:
                    apart_idx = i
                nums[i] = num ** 2
            else:
                negative_part.append(num ** 2)

        positive_idx = apart_idx
        negative_idx = apart_idx - 1

        # combine two part
        i = 0
        while positive_idx < len(nums) and negative_idx >= 0:
            if nums[positive_idx] < negative_part[negative_idx]:
                nums[i] = nums[positive_idx]
                positive_idx += 1
            else:
                nums[i] = negative_part[negative_idx]
                negative_idx -= 1
            i += 1
        while positive_idx < len(nums):
            nums[i] = nums[positive_idx]
            i += 1
            positive_idx += 1
        while negative_idx >= 0:
            nums[i] = negative_part[negative_idx]
            i += 1
            negative_idx -= 1
        return nums


if __name__ == '__main__':
    print(Solution().sortedSquares([-2, 0]))
