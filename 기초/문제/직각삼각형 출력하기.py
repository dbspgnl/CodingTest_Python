n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()

"""
# 방법1. 
n = int(input())
for i in range(1,n+1):
    print('*'*i)
# 방법2.
print('\n'.join('*' * (i + 1) for i in range(int(input()))))
"""

