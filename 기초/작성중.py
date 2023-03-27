# from fractions import Fraction
# def solution(numer1, denom1, numer2, denom2):
#     return Fraction(numer1, denom1) + Fraction(numer2, denom2)
def solution(n):
    return sum(int(i) for i in str(n))

print(solution(1234))

def re(i):
    if i is None or i == "": return re(i)
    return i
def test():
    ios = ""
    if ios is None or ios == "":
        print("ios는 널이다.")
    else:
        print("걸러내지 못함")
    # ---
    array = ["a", "", "b", ""]
    for i in array:
        print(re(i))

test()