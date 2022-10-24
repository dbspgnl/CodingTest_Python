"""
입력 글자 수 n = 11
글자 수 만큼 숫자 입력 10987654321
"""


n = input()
numbers = list(input())
sum = 0

for i in numbers:
    sum = sum+int(i) # numbers에서 각 자리수를 가져와서 더하기

print(sum)