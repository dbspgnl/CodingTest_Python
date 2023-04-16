def solution(sizes):
    w = 0
    h = 0
    for size in sizes:
        w = max(w, max(size))
        h = max(h, min(size))
    return w*h

# 80*50 = 4000
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]])) # 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) # 120