if __name__ == '__main__':
    while True:
        try:
            s = input()
            for i in range(0, len(s), 8):
                print("{0:0<8s}".format(s[i:i + 8]))
        except:
            break
