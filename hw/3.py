if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            data = [int(input()) for i in range(n)]
            for i in sorted(set(data)):
                print(i)
        except:
            break
