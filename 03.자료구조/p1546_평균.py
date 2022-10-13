"""
내 점수들 중에서 최고 점수를 구해서
모든 점수를 점수/최고점수*100으로 변경해서 평균을 구한다.
----
2
3 10
= 65.0
"""
n = input()
mylist = list(map(int, input().split()))
mymax = max(mylist) # 최고 점수
sum = sum(mylist)
print(sum*100/mymax/int(n))
