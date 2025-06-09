# https://medium.com/starbugs/python-%E4%B8%80%E6%AC%A1%E6%90%9E%E6%87%82-pass-by-value-pass-by-reference-%E8%88%87-pass-by-sharing-1873a2c6ac46

obj = {"name": "Harry", "age": 26}


# === 更改obj 的function =====
def function_change(obj):
    print(f"Before the variable assign , the obj is:{obj}")
    obj["name"] = "Lulu"
    obj["age"] = 31
    print(f"After the variable assign , the obj is:{obj}")


print(f"Before the variable assign , the obj is:{obj}")
function_change(obj)
print(f"After the variable assign , the obj is:{obj}")


# 一樣，我們先把記憶體位址印出來試試看。
def function_change2(obj):
    print(f"Before the variable assign , the obj is:{id(obj)}")
    obj["name"] = "Lulu"
    obj["age"] = 31
    print(f"After the variable assign , the obj is:{id(obj)}")


print(f"Before the variable assign , the obj is:{id(obj)}")
function_change2(obj)
print(f"After the variable assign , the obj is:{id(obj)}")

# =====
# 記憶體位址完全沒有改變，
# 這是為什麼呢？
# 因為剛剛我們使用字典 (dict) 這種資料型別
# 是屬於可變物件 (Mutable Object)，內容可以改變
# =======


##==== 看用immutabe物件 ======
weight = 70
height = 1.7


def getBMI(w, h):
    bmi = w / pow(h, 2)
    print(f"befroe bmi:{bmi}")
    w = 80
    h = 1.8
    bmi = w / pow(h, 2)
    print(f"weight:{w}")
    print(f"height:{h}")
    print(f"after bmi:{bmi}")


getBMI(weight, height)
print(f"outside weight:{weight}")  # 還是沒變
print(f"outside height:{height}")  # 還是沒變


# ===== mutable ======
list1 = [1, 2, 3]


def addList(li):
    print(f"before list:{li}")
    li.append(4)
    print(f"after list:{li}")


print(f"before addList : {list1}")
addList(list1)
print(f"after addList : {list1}")  # 因為是mutable 所以被改動了

# ======
# mutable , immutabe 參考位置範例
# =======
a = [3, 4, 5]
b = a
print(
    f"記憶體位置a,b一樣嗎? {id(a) == id(b)}"
)  # -->記憶體裡存a跟b 的data指向的資料位置相同

b = [4, 5, 6]  # 更改記憶體data指向位置
print(a)
print(b)

coffe = "Latte"
cafe = coffe
print(f"記憶體位置a,b一樣嗎? {id(coffe) == id(cafe)}")
coffe = "Americano"
print(f"coffe:{coffe}")
print(f"cafe:{cafe}")
