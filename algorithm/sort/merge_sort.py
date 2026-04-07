def merge(nums_1, nums_2):
    """

    Args:
        nums_1 ():
        nums_2 ():

    Returns:

    """
    temp = []
    idx_1, idx_2 = 0, 0
    while idx_1 < len(nums_1) and idx_2 < len(nums_2):
        if nums_1[idx_1] <= nums_2[idx_2]:
            temp.append(nums_1[idx_1])
            idx_1 += 1
        else:
            temp.append(nums_2[idx_2])
            idx_2 += 1

    if idx_1 < len(nums_1):
        temp.extend(nums_1[idx_1:])
    if idx_2 < len(nums_2):
        temp.extend(nums_2[idx_2:])
    return temp


def merge_sort_recursive(nums, start, end):
    """

    Args:
        nums (list):
        start (int):
        end (int):

    Returns:

    """
    # end condition
    if start == end:
        return
    # top -> down
    mid = start + (end - start) // 2
    # merge
    merge_sort_recursive(nums, start, mid)
    merge_sort_recursive(nums, mid + 1, end)
    nums[start:end + 1] = merge(nums[start:mid + 1], nums[mid + 1:end + 1])


def merge_sort_while(nums, start, end):
    """

    Args:
        nums (list):
        start (int):
        end (int):

    Returns:

    """
    # down -> top
    step = 2
    while step <= len(nums) * 2:
        for i in range(0, len(nums), step):
            start = i
            mid = i + step // 2 - 1
            end = min(i + step - 1, len(nums) - 1)
            nums[start:end + 1] = merge(nums[start:mid + 1], nums[mid + 1:end + 1])
        step *= 2


if __name__ == '__main__':
    unsorted = [5, 2, 5, 7, 1, 6, 0, 8]
    merge_sort_while(unsorted, 0, len(unsorted) - 1)
    print(unsorted)
