if __name__ == '__main__':
    n = int(input())
    n_set = set()
    res = []
    while n:
        t = n % 10
        if t not in n_set:
            n_set.add(t)
            res.append(t)
        n //= 10
    r = 0
    for i in range(len(res)):
        r += res[i] * (10 ** (len(res) - i -1))
    print(r)
