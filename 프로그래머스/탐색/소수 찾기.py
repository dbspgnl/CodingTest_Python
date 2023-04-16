from itertools import permutations
import math

def primenumber(x):
    for i in range (2, int(math.sqrt(x) + 1)):	
    	if x % i == 0:
            return False
    return True

def solution(numbers):
    per = list(permutations(list(numbers)))
    num_list = [''.join(p) for p in per]
    num_list += list(numbers)
    num_list = set(num_list)
    num_list.discard("0")
    num_list.discard("1")
    count = 0
    for num in num_list:
        i = int(num)
        if primenumber(i): count +=1
    return count

print(solution("17")) #3
print(solution("011")) #2