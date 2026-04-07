def get_next(s):
    """
    generate next arr for kmp

    Args:
        s ():

    Returns:

    """
    next_arr = [-1] * len(s)

    j = -1
    for i in range(1, len(s)):
        # find 公共前后缀的长度 - 1
        while j >= 0 and s[i] != s[j + 1]:
            # 跳到上个前后缀相同到索引上，就是s_{0->j} == s_{i-1,i-1-j}
            # 为什么这样能跳？
            # 首先next_arr[i]保存的是s_{0->i}的公共前后缀长度 - 1
            # 也就是前缀的索引
            # 当s[i] != s[j+1]时
            # 我们要缩短公共前后缀的长度进行尝试
            j = next_arr[j]
        if s[i] == s[j + 1]:
            j += 1
        next_arr[i] = j
    return next_arr


def kmp(source, target):
    """

    Args:
        source (str):
        target (str):

    Returns:

    """
    if len(target) == 0:
        return 0

    # get next
    next_arr = get_next(target)

    # find target
    j = -1
    for i in range(len(source)):
        # 如果当前匹配的不对，即source[i] != target[j + 1]
        # 那么根据前后缀的相同，可以避免一部分的重新匹配
        while j >= 0 and source[i] != target[j + 1]:
            j = next_arr[j]
        if source[i] == target[j + 1]:
            j += 1
        if j == len(target) - 1:
            return i - j
    return -1


if __name__ == '__main__':
    print(kmp(source="vabaa", target="aba"))
