if __name__ == '__main__':
    n = int(input())
    count = 0
    while n:
        if n & 1:
            count += 1
        n >>= 1
    print(count)