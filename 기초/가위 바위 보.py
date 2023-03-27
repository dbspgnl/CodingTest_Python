# 가위는2 바위는0 보는5 일 때 입력한 값을 이기는 값 출력
def solution(rsp):
    answer = ''
    for w in list(rsp):
        if w == "2": answer += "0"
        if w == "0": answer += "5"
        if w == "5": answer += "2"
    return answer

print(solution("2")) # 0
print(solution("205")) # 052

"""
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)
"""