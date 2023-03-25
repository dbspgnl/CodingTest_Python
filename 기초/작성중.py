from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    return Fraction(numer1, denom1) + Fraction(numer2, denom2)

print(solution(1,2,3,4))

"""
def solution(s1, s2):
    return len(set(s1)&set(s2));

   
def solution(numer1, denom1, numer2, denom2):
    answer = []
    return answer

print(solution(1,2,3,4))
"""

