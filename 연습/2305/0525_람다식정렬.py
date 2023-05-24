# b 데이터를 오름차순으로 해서 a의 위에서 2개 까지만 출력
a_dict = {'a': [0,2,3], 'b':[1,4]}
b_dict = {0: 100, 2: 500, 3: 300} # 2,3,0
# print(a_dict['a']) # [0,2,3]
a_sort = sorted(a_dict['a'], key=lambda x: (-b_dict[x], x))
print(a_sort[:2])

