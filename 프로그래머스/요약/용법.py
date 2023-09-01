# === zip ===
# 배열을 교차해서 처리
a,b,c = [1, 2, 3],[4, 5, 6],[7, 8, 9]
for i, j, k in zip(a, b, c):
    print(i, j, k)

# 따라서 두 개의 배열을 순차적으로 비교해볼 수 있다.
for p1, p2 in zip(["6", "12", "6789"], ["6", "12", "6789"][1:]):
    if p2.startswith(p1): pass

# === get ===
# 해시맵에 값이 있으면 처리
hash_map = {}
for clothe, type in [["yellohat", "headgear"],["bluesunglasses", "eyewear"]]:
	hash_map[type] = hash_map.get(type, 0) +1 # 두번째 type이 있으면 카운팅

# === enumerate ===
# 배열을 쉽게 index가 있는 튜플로 변경할 수 있다.
e = list(enumerate(list("abcdefghij")))
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), ... ]

# === deque ===
from collections import deque
q1 = deque([1, 2, 3])
q1.rotate(1) # 양수면 시계방향 [3, 1, 2]
q1.rotate(-1) # 음수면 반시계 [2, 3, 1]
q1.append(4) # 뒤로 추가
q1.popleft() # 앞에서 꺼냄 / 뒤로 꺼냄 pop()


# === not in (contain) ===
# 손쉽게 포함여부를 판단할 수 있다.
result = []
for w in list("We are the world"):
    if w not in result: result.append(w)

# === bin ===
# 진수 변환은 int와 bin으로 쉽게 한다.
int("101",2) # 5
bin(5) # 0b101

# === permutations, combinations ===
from itertools import combinations, permutations
perm = list(permutations([1, 2, 3]))
print(perm) # (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)
nums = [1, 2, 3, 4]
combi = list(combinations(nums, 2))
print(combi) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]


# 등차/등비 수열 구하기
def solution(common):
    for n1, n2, n3 in zip(common, common[1:], common[2:]):
        if n2 + (n2 - n1) == n3:
            return int(common[-1] + (n2 - n1))
        elif n2 * (n2 / n1) == n3:
            return int(common[-1] * (n2 / n1))
print(solution([1,2,3,4])) # 5
print(solution([2,4,8])) # 16

#  === isdigit() ===
# 글자 중에서 숫자들만 종합해서 int로 치환후 합하는 방법
numb1 = sum(int(i) for i in "a1b2c3d4" if i.isdigit())
print(numb1) # 10

# === count() ===
print(["a", "b", "c", "a"].count("a")) # 2

# 중복 확인
print(len(set([1,2,3,4])&set([1,2,4]))) # 3

# 뒤집기
print(list(reversed(["a","b","c","d","e"]))) # resersed는 obj로 반환됨

# 대소문자 처리
print("ccc".upper())
print("CCC".lower())

# 짝수만 걸러서 더하기
n = 10
print(sum([i for i in range(2, n + 1, 2)])) # (시작, 끝, 간격)

# map + len 사용한 배열의 각 문자열 길이
print(list(map(len,["abc", "efgh", "ijklm"]))) # [3,4,5]

# 람다식
print(list(filter(lambda x: x % 2 == 0, range(10)))) # [0, 2, 4, 6, 8]

# key와 value 스왑
di = dict(zip('abcde', range(5)))
print(di) # {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
swap = [(i[1],i[0]) for i in di.items()] # key와 value 변경
print(swap)# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

# 문자열 안에 숫자를 찾아내기
parse_list = "".join([word if word.isnumeric() else ' ' for word in list("aAb1B2cC34oOp")])
print(parse_list) # "   1 2  34   "
number_list = list(map(int, parse_list.split())) # split으로 빈 공간을 없애줌
print(number_list) #[1, 2, 34]

# 문자열 역순
print("abcdefg"[::-1])

# 배열을 딕셔너리에 담아주기
key, i = "a", 1
dicts = {}
if key not in dicts: # 새로 만들어주기
  dicts[key] = [i]
else: # 있으면 기존에 넣기
  dicts[key].append(i) # 기존에 추가

# all any
# 모든 요소가 모두 참이면  all 하나라도 참이면 any를 사용한다.
queue = [(0,2),(1,1),(2,3),(3,2)]
first = queue.pop(0) # (0,2)(1,1)(2,3)(3,2)
if any(first[1] < q[1] for q in queue):
    queue.append(first)
    print(queue)