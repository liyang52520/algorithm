def quick_sort(nums, start, end):
    """

    Args:
        nums (list):
        start (int):
        end (int):

    Returns:

    """
    if start >= end:
        return
    left, right = start, end
    mid_num = nums[start]
    while True:
        while left <= right:
            if nums[left] > mid_num:
                break
            left += 1
        while left <= right:
            if nums[right] <= mid_num:
                break
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
        else:
            nums[right], nums[start] = nums[start], nums[right]
            break
        left += 1
        right -= 1
    quick_sort(nums, start, right - 1)
    quick_sort(nums, right + 1, end)


if __name__ == '__main__':
    unsorted = [5, 2, 3, 1, 3, 5, 7, 1, 6, 0, 8]
    quick_sort(unsorted, 0, len(unsorted) - 1)
    print(unsorted)
