def solve(highs):
    """

    Args:
        highs (list):

    Returns:

    """
    # left[i] 代表了以highs[i]为结尾的最长递增序列的长度
    left = [1] * len(highs)
    # right[i] 代表了以highs[i]为开头的最长递减序列的长度
    right = [1] * len(highs)
    for i in range(len(highs)):
        # get lower
        for j in range(i):
            if highs[j] < highs[i]:
                left[i] = max(left[i], left[j] + 1)
    for i in range(len(highs) - 1, -1, -1):
        # get higher
        for j in range(i + 1, len(highs)):
            if highs[j] < highs[i]:
                right[i] = max(right[i], right[j] + 1)
    max_len = 0
    for i in range(len(highs)):
        max_len = max(max_len, left[i] + right[i] - 1)
    print(len(highs) - max_len)


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            data = list(map(int, input().split()))[:n]
            solve(data)
        except:
            break

