# https://www.nowcoder.com/questionTerminal/42852fd7045c442192fa89404ab42e92?
def check_str(strs):
    res = []
    for char in strs:
        if len(res) < 2:
            res.append(char)
            continue
        if len(res) >= 2:
            if char == res[-1] and char == res[-2]:
                continue
        if len(res) >= 3:
            if char == res[-1] and res[-2] == res[-3]:
                continue
        res.append(char)
    print("".join(res))


check_str("helllo")
