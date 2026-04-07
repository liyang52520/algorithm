if __name__ == '__main__':
    k_v = {}
    n = int(input())
    for i in range(n):
        k, v = list(map(int, input().split()))
        k_v[k] = k_v.get(k, 0) + v
    res = sorted(k_v.items(), key=lambda x: x[0])
    for k, v in res:
        print("{} {}".format(k, v))
