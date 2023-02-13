list = []
for i in range(4):
    list.append({"key":i, "name":"홍"+str(i*10)})

for item in list:
    if item["key"] == 1:
        print(item)
        item["name"] = "김철수"
        print(item)
print(list)
print("----")

for item in list:
    print(item.get("key"))
    if 2 == item.get("key"):
        print("해당 키는 존재합니다.")
    else:
        print("키가 없습니다.")