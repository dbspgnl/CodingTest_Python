def solution(polynomial):
    split = polynomial.split(" + ")
    x = 0
    num = 0
    for word in split:
        if word != "0":
            if "x" in word:
                if word == "x":
                    x+=1
                else:
                    x += int(word.split("x")[0])
            else:
                num += int(word)
    if x == 0:
        return str(num)
    elif num == 0:
        return str(x)+"x" if x !=1 else "x"
    else:
        return str(x)+"x + "+str(num) if x !=1 else "x + "+str(num)

print(solution("3x + 7 + x")) # "4x + 7"
print(solution("x + 0"))