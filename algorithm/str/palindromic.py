def palindromic(s):
    """

    Args:
        s:

    Returns:

    """
    results = []
    dp = [[False
           if i != j else True for j in range(len(s))]
          for i in range(len(s))]
    results.extend(s)
    for step in range(2, len(s) + 1):
        for i in range(len(s) - step + 1):
            j = i + step - 1
            if s[i] == s[j]:
                if step == 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    results.append(s[i:j + 1])
    return results


if __name__ == '__main__':
    print(palindromic("aaa"))
