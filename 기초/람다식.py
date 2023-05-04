a = [(1, 2), (5, 1), (0, 1), (5, 2), (3, 0)]

# 일반 정렬
b = sorted(a) # 앞의 인자로 정렬됨
print(b)
#b = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

# key인자로 우선순위 정하기
c = sorted(a, key = lambda x : x[0])
print(c)
#c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]
d = sorted(a, key = lambda x : x[1])
print(d)
#d = [(3, 0), (5, 1), (0, 1), (1, 2), (5, 2)]

# key로 복수 비교, -를 붙여서 반대차순 정렬
e = sorted(a, key = lambda x : (x[0], -x[1]))
print(e)
# [(0, 1), (1, 2), (3, 0), (5, 2), (5, 1)]
f = sorted(a, key = lambda x : -x[0])
print(f)
# [(5, 1), (5, 2), (3, 0), (1, 2), (0, 1)])

# 문자열 정렬
s = ['2 A', '1 B', '4 C', '1 A']
g = sorted(s, key=lambda x: (x.split()[1], x.split()[0]))
print(g)
# ['1 A', '2 A', '1 B', '4 C']
# 카운터를 이용한 정렬
from collections import Counter
a_list = ['a', 'b', 'd', 'd', 'b','s']
a_counter = Counter(a_list).most_common()
# [('b', 2), ('d', 2), ('a', 1), ('s', 1)]
# 문자 역순(아스키 값 이용)
sorted(a_counter,  key=lambda x: (-x[1], -ord(x[0])))
# [('d', 2), ('b', 2), ('s', 1), ('a', 1)]

# map()으로 람다식 담기
print(list(map(lambda x: x+10, [1,2,3])))
#[11, 12, 13]

# filter()로 특정 값만 담기
a = [8, 4, 2, 5, 2, 7, 9, 11, 26, 13]
result = list(filter(lambda x : x > 7 and x < 15, a))
print(result)
# [8, 9, 11, 13]

# reduce()로 특정 식으로 누적시키기
from functools import reduce
t = [47, 11, 42, 13]
result2 = reduce(lambda x, y : x + y, t) # 앞 뒤로 더하면서 누적
print(result2)
# 113