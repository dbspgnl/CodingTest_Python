def solution(price):
    if price >= 500000:
        return int(price*0.8)
    if price >= 300000:
        return int(price*0.9)
    if price >= 100000:
        return int(price*0.95)
    return price

print(solution(150000))
print(solution(580000))
print(solution(400000))
print(solution(10))
print(solution(1000000))

"""
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
"""

