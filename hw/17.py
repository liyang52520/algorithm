
if __name__ == '__main__':
    actions = input().split(";")
    # filter actions
    res = [0, 0]
    for action in actions:
        if len(action) == 2 or len(action) == 3:
            if action[0] in "WASD" and action[1:].isdigit():
                x = int(action[1:])
                if action[0] == "W":
                    res[1] += x
                elif action[0] == "S":
                    res[1] -= x
                elif action[0] == "A":
                    res[0] -= x
                else:
                    res[0] += x
    print("{},{}".format(res[0], res[1]))
