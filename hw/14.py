if __name__ == '__main__':
    n = int(input())
    data = [input() for _ in range(n)]
    for i in sorted(data):
        print(i)