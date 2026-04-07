def check(s):
    if len(s) <= 8:
        return False
    type_check = [0, 0, 0, 0]
    couple = {}
    for i in range(len(s)):
        if str.islower(s[i]):
            type_check[0] = 1
        elif str.isupper(s[i]):
            type_check[1] = 1
        elif str.isdigit(s[i]):
            type_check[2] = 1
        elif s[i] != " " and s[i] != "\n":
            type_check[3] = 1
        if i >= 2:
            c_couple = s[i-2:i+1]
            if c_couple not in couple:
                couple[c_couple] = i
            else:
                if couple[c_couple] < i - 2:
                    return False
    return sum(type_check) >= 3


if __name__ == '__main__':
    # while True:
    #     try:
    #         if check(input()):
    #             print("OK")
    #         else:
    #             print("NG")
    #     except:
    #         break
    print(check("7v0T+6s!(7*)C4RX8*IB85yk+6&~#v6)q$+W3&8-8+"))
