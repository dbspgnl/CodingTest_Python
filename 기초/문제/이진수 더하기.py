def solution(bin1, bin2):
    return str(bin((int(bin1,2) + int(bin2,2)))).replace("0b", "")

print(solution("10", "11"))

"""
def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer
"""