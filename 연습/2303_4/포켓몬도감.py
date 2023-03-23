# 기본적인 해시문제
import sys
input = sys.stdin.readline
n,m = map(int, input().split())

idx_to_name = {}
name_to_idx = {}
for i in range(1, n+1):
    name = input().rstrip()
    idx_to_name[i] = name
    name_to_idx[name] = i

for _ in range(m):
    query = input().rstrip()
    if query.isdigit():
        print(idx_to_name[int(query)])
    else:
        print(name_to_idx[query])

"""
3 3
이상해씨 
파이리 
꼬북이
1
파이리
3
"""
