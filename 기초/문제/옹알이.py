def solution(babbling):
    result = 0
    dic =["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for d in dic:
            babbling[i] = babbling[i].replace(d, "0")
        if babbling[i].isdigit() and int(babbling[i]) == 0:
            result +=1
        print(babbling)
    return result


print(solution(["aya", "yee", "u", "maa", "wyeoo"])) #1
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])) #3