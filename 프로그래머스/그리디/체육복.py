def solution(n, lost, reserve):
    reverse_only = set(reserve) - set(lost)
    lost_only = set(lost) - set(reserve)
    for r in reverse_only:
        front = r -1 # 앞 인덱스
        back = r +1 # 뒤 인덱스
        if front in lost_only: # 앞 사람이 체육복 없는 사람에 해당하면
            lost_only.remove(front) # 옷을 주기 때문에 없는 명단에서 제거
        elif back in lost_only:
            lost_only.remove(back)
    return n - len(lost_only) # 전체에서 옷 없는 사람 수 빼면 = 옷 있는 사람

print(solution(5,[2, 4],[1, 3, 5])) #5
print(solution(5,[2, 4],[3])) #4
print(solution(3,[3],[1])) #2