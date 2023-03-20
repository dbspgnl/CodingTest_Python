from itertools import permutations # 리스트 내용으로 모든 조합을 짜준다.
def solution(numbers):
    prime_set = set()
    # 1. 모든 숫자 조합을 만든다.
    for i in range(len(numbers)):
        # print(list(numbers)) # 1,7,17,71
        numbers_permutation = permutations(list(numbers), i+1) # 순열로 처리해줌
        # print(list(map("".join, numbers_permutation)))
        numbers_perm_list = list(map(int, map("".join, numbers_permutation)))
        prime_set |= set(numbers_perm_list)
        print(prime_set) # {1,71,17,7}
    # 2. 소수가 아닌 수를 제외한다.
    prime_set -= set(range(0,2)) # 앞부분 제거 0,1
    lim = int(max(prime_set) ** 0.5) +1
    for i in range(2, lim):
        prime_set -= set(range(i*2,max(prime_set)+1,i))

    return print(prime_set)

solution("17")