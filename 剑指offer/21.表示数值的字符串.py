def aa(s):
    isAllowdot = True
    isAllowE = True

    for i in range(len(s)):
        if (s[i] in "+-" and i == 0) or (s[i-1] in "eE" and i < len(s)-1):
            continue
        elif isAllowdot and s[i] == ".":
            isAllowdot = False
            if i >= len(s)-1 or s[i+1] not in "0123456789":
                return False
        elif isAllowE and s[i] in"eE":
            isAllowdot = False
            isAllowE = False
            if i >= len(s)-1 or s[i+1] not in "0123456789+1":
                return False
        elif s[i] not in "0123456789":
            return False
    return True
