class Item:
    def __init__(self, val, weight, par):
        self.val = val
        self.weight = weight
        self.par = par
        self.res = self.val * self.weight
        self.children = [None, None]
        self.child_count = 0

    def add_child(self, item):
        self.children[self.child_count] = item
        self.child_count += 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    items = []
    for i in range(m):
        v, p, q = map(int, input().split())
        items.append(Item(v, p, q - 1))
    main_items = []
    for item in items:
        if item.par != -1:
            items[item.par].add_child(item)
        else:
            main_items.append(item)

    # dp的意义是最多钱数为n时的最大结果
    dp = [0] * (n + 1)

    for item in main_items:
        for c in range(n, -1, -1):
            if c >= item.val:
                dp[c] = max(dp[c], dp[c - item.val] + item.res)
            if item.children[0] is not None and c >= item.val + item.children[0].val:
                dp[c] = max(dp[c], dp[c - item.val - item.children[0].val] + item.res + item.children[0].res)
            if item.children[1] is not None and c >=item.val + item.children[1].val :
                dp[c] = max(dp[c], dp[c - item.val - item.children[1].val] + item.res + item.children[1].res)
            if item.children[1] is not None and item.children[0] is not None and c >= item.val + item.children[0].val + item.children[1].val:
                dp[c] = max(dp[c],
                            dp[c - item.val - item.children[0].val - item.children[1].val] + item.res + item.children[
                                1].res + item.children[0].res)
    print(dp[n])
