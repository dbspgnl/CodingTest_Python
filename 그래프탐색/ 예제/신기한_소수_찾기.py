"""
숫자 N이 주어졌을 때 N의 자리 숫자 중 신기한 소수를 찾기
신기한 소수 = 각 자리 수가 모두 소수인 case
근데 1의 자리 소수는 4개밖에 없다. (10자리부터는 1도 포함)
따라서 2,3,5,7에 대한 1,3,5,7,9의 N자리 만큼 DFS로 탐색하면서 소수 여부를 파악하면 된다.

"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input()) # 1이상 8이하

# 소수 구하기 확인
def isPrime(num):
    #for i in range(2, int(num)): # num까지 전부 확인하기
    #for i in range(2, int(num//2+1)): # num/2까지 소수 횟수 낮추기
    for i in range(2, int(num**0.5)+1): # num의 제곱근까지 나누기
    # 에라토스테네스의 체 방식도 있다.
        if num % i == 0: # 21%2 ==0
           return False
    return True

# DFS
def DFS(number):
    if len(str(number)) == N: # 자리수가 늘어나다가 N자리수가 되면 print하고 종료
        print(number)
    else:
        for i in range(1,10):
            if i % 2 == 0: continue # 소수는 짝수가 없음으로 거르기
            if isPrime(number * 10 + i): # 소수 체크 2라면 21,22,23..30까지 체크
                DFS(number*10+i)

DFS(2) #2번으로 시작하는 구간 탐색
DFS(3) #3번으로 시작하는 구간 탐색
DFS(5) #5번으로 시작하는 구간 탐색
DFS(7) #7번으로 시작하는 구간 탐색

"""
4
= 2333
2339
2393
2399
2939
3119
3137
3733
3739
3793
3797
5939
7193
7331
7333
7393
"""