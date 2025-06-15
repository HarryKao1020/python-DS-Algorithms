##======= list =======
array1 = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "lemon", "apple"]
for i in array1:
    print(i)

for fruit in fruits:
    print(fruit)

##修改元素
fruits[3] = "orange"
print(fruits[3])


##添加元素
array1.append(6)
print(array1)

array1.append(50)

##插入元素
array1.insert(2, 2.5)
print(array1)

# remove元素
array1.remove(2.5)
print(array1)

##====== Tuple  =======
# 在 Python 中，tuple（元組）是一種有序的、不可變的集合，用於存儲多個元素。元組和列表類似，但元組一旦創建就不能修改，這使得元組在需要一個不可變的數據集合時特別有用。元組用圓括號 () 表示，元素之間用逗號分隔。
array2 = (1, 2, 3, 4, 5, 1)
print("array2:", array2)

# single element 要加,
single_element_tuple = (1,)
print("signle_ele:", single_element_tuple[0])
# count()：返回某個值在元組中出現的次數
# index()：返回某個值在元組中的索引位置（若存在多個，返回第一次出現的位置）
print("count:", array2.count(1))
print("index:", array2.index(3))

# 在 Python 中，set（集合）是一種無序且不重複的元素集合。集合主要用於需要存儲唯一項目的情況，可以高效地進行成員測試、去重和集合運算（如並集、交集和差集）。
color = {"red", "green", "blue", "purple"}
# 使用 set() 函數創建集合
numbers = set([1, 2, 3, 4, 5])

# 空集合只能用 set() 函數創建
empty_set = set()

for y in color:
    print(y)

# 添加元素 add,加單一元素
color.add("orange")

# 使用 update() 方法添加多個元素
color.update(["black", "white"])
print(color)

# remove & discard & pop
# 使用 remove() 方法移除元素（若元素不存在，會引發 KeyError）
color.remove("black")
print(color)

# 使用 discard() 方法移除元素（若元素不存在，不會引發錯誤）
color.discard("blue")
print(color)

# 使用 pop() 方法移除並返回一個隨機元素
removed_color = color.pop()
print(removed_color)
print(color)

# 在 Python 中，dict（字典）是一種無序的、可變的鍵值對集合。每個鍵（key）是唯一的，並且與一個值（value）相關聯。字典用大括號 {} 表示，鍵和值之間用冒號 : 分隔，鍵值對之間用逗號分隔。
person = {"name": "Harry", "age": 18, "gender": "male"}
print(person["name"])
# 添加鍵值對
person["job"] = "engineer"
print(person)

# 使用 del 關鍵字刪除鍵值對
del person["age"]
print(person)

keys = person.keys()
print(keys)

value = person.values()
print(value)

item = person.items()
print(item)

# 迭代鍵
for key in person:
    print("key", key, person[key])

# 迭代值
for value in person.values():
    print("value", value)

# 迭代鍵值對
for key, value in person.items():
    print("key value", key, value)
