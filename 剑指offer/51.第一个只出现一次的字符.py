# 在字符串中找出第一个只出现一次的字符
# 入输入 "abacasdfadasdfaseff" 则输出b


strs = "abaaccc"


def findOne(strs):
    if not strs:
        return

    record = []
    for ss in strs:
        if ss not in record:
            record.append(ss)
        else:
            record.remove(ss)
    return record[0]


print(findOne(strs))
