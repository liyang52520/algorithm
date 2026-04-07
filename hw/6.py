import math

if __name__ == '__main__':
    n = int(input())
    # get all 质数
    y = 2
    res = []
    up = math.sqrt(n) + 1
    while y <= up:
        if n % y == 0:
            res.append(str(y))
            n /= y
        else:
            y += 1
    if n != 1:
        res.append(str(int(n)))
    print(" ".join(res) + " ")

