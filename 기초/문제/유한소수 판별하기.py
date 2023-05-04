from math import gcd
def solution(a, b):
    b //= gcd(a,b) #바로 최대공약수부터 구해서 나눈 값을 넣기
    while b%2==0:
        b//=2  #2로 나누어 떨어지면 2로 나눈 값 넣기
    while b%5==0:
        b//=5 #5로 나누어 떨어지면 5로 나눈 값 넣기
    return 1 if b==1 else 2 #다 나누어 떨어지면 1,아니면 2넣기

print(solution(7,20)) #1
print(solution(11,22)) #1
print(solution(12,21)) #2
print()
print(solution(30,3)) #1
print(solution(40,30)) #2
print(solution(30,40)) #1
print()
print(solution(3,30)) #1
print(solution(30,30)) #1




