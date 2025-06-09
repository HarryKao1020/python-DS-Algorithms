**Pass by Assignment** 是對的，而且可能是最準確的描述。讓我解釋為什麼：

### pass by assignment
| 簡單來說就是有pass by value 也有 pass by reference

根據資料的型別是mutable還是immutable決定

## Pass by Assignment vs Call by Object Reference


這兩個術語實際上描述的是同一個概念，但 **Pass by Assignment** 更準確地反映了 Python 的實際行為。

### 為什麼叫 Pass by Assignment？

在 Python 中，參數傳遞的行為就像執行賦值語句一樣：

```python
def func(param):
    # 這相當於執行: param = argument
    pass

# 當你呼叫 func(my_var) 時
# 實際上就像執行: param = my_var
```

## 理解 Assignment 的行為

### 賦值就是建立參考
```python
# 基本賦值行為
a = [1, 2, 3]
b = a  # 這不是複製，而是讓 b 參考同一個物件

print(id(a) == id(b))  # True - 同一個物件
b.append(4)
print(a)  # [1, 2, 3, 4] - a 也被修改了

# 函數參數傳遞的行為完全相同
def modify_list(lst):  # lst = original_list (賦值)
    lst.append(4)

original_list = [1, 2, 3]
modify_list(original_list)
print(original_list)  # [1, 2, 3, 4]
```

### 重新賦值會改變參考
```python
# 重新賦值的行為
a = [1, 2, 3]
b = a
print(id(a) == id(b))  # True

b = [4, 5, 6]  # 重新賦值，b 現在參考新物件
print(id(a) == id(b))  # False
print(a)  # [1, 2, 3] - a 沒有改變

# 函數中的重新賦值也是如此
def reassign_list(lst):  # lst = original_list (賦值)
    lst = [4, 5, 6]      # lst = new_list (重新賦值)
    # 現在 lst 參考新物件，與原始物件無關

original_list = [1, 2, 3]
reassign_list(original_list)
print(original_list)  # [1, 2, 3] - 沒有改變
```

## 詳細比較不同的傳遞方式

### Call by Value (真正的值傳遞)
```python
# 如果 Python 是 call by value，會是這樣：
def hypothetical_call_by_value(lst):
    # lst 會是 original_list 的完整副本
    lst.append(4)  # 只修改副本

# 但 Python 不是這樣工作的！
```

### Call by Reference (真正的參考傳遞)
```python
# 如果 Python 是 call by reference，會是這樣：
def hypothetical_call_by_reference(lst):
    lst = [4, 5, 6]  # 這會直接修改原始變數
    # 原始變數也會變成 [4, 5, 6]

# 但 Python 也不是這樣工作的！
```

### Pass by Assignment (Python 的實際行為)
```python
def python_actual_behavior(lst):  # lst = original_list
    # lst 現在參考與 original_list 相同的物件
    lst.append(4)     # 修改該物件 ✓
    lst = [4, 5, 6]   # lst 重新賦值，參考新物件
    # 原始變數仍然參考原物件

original_list = [1, 2, 3]
python_actual_behavior(original_list)
print(original_list)  # [1, 2, 3, 4] - 只有 append 生效
```

## 用賦值來理解各種情況

### 情況 1: Immutable 物件
```python
# 等同的賦值行為
x = 5
y = x  # y 參考相同的物件
y = y + 1  # y 重新賦值到新物件 (6)
print(x)  # 5 - 沒有改變

# 函數版本
def add_one(num):  # num = x (賦值)
    num = num + 1  # num 重新賦值到新物件
    return num

x = 5
result = add_one(x)
print(x)      # 5 - 沒有改變
print(result) # 6
```

### 情況 2: Mutable 物件的修改
```python
# 等同的賦值行為
list1 = [1, 2, 3]
list2 = list1  # list2 參考相同物件
list2.append(4)  # 修改該物件
print(list1)  # [1, 2, 3, 4] - 被修改

# 函數版本
def append_item(lst):  # lst = list1 (賦值)
    lst.append(4)      # 修改該物件

list1 = [1, 2, 3]
append_item(list1)
print(list1)  # [1, 2, 3, 4] - 被修改
```

### 情況 3: Mutable 物件的重新賦值
```python
# 等同的賦值行為
list1 = [1, 2, 3]
list2 = list1      # list2 參考相同物件
list2 = [4, 5, 6]  # list2 重新賦值到新物件
print(list1)       # [1, 2, 3] - 沒有改變

# 函數版本
def replace_list(lst):  # lst = list1 (賦值)
    lst = [4, 5, 6]     # lst 重新賦值到新物件

list1 = [1, 2, 3]
replace_list(list1)
print(list1)  # [1, 2, 3] - 沒有改變
```

## 實際驗證：物件 ID 追蹤

```python
def trace_assignment():
    # 模擬函數參數傳遞
    original = [1, 2, 3]
    print(f"Original ID: {id(original)}")
    
    # 這就是函數參數傳遞時發生的事
    param = original  # 賦值：param = original
    print(f"Param ID after assignment: {id(param)}")
    print(f"Same object? {id(param) == id(original)}")
    
    # 修改物件
    param.append(4)
    print(f"After modification - Original: {original}")
    print(f"After modification - Param ID: {id(param)}")
    print(f"Still same object? {id(param) == id(original)}")
    
    # 重新賦值
    param = [5, 6, 7]
    print(f"After reassignment - Original: {original}")
    print(f"After reassignment - Param ID: {id(param)}")
    print(f"Still same object? {id(param) == id(original)}")

trace_assignment()
```

輸出：
```
Original ID: 140234567890123
Param ID after assignment: 140234567890123
Same object? True
After modification - Original: [1, 2, 3, 4]
After modification - Param ID: 140234567890123
Still same object? True
After reassignment - Original: [1, 2, 3, 4]
After reassignment - Param ID: 140234567890456
Still same object? False
```

## 結論

**Pass by Assignment** 是更準確的描述，因為：

1. **它直接反映了 Python 的實際機制**：參數傳遞就像賦值操作
2. **避免了術語混淆**：不會與傳統的 "call by reference" 或 "call by value" 混淆
3. **更容易理解**：如果你理解 Python 的賦值，就能理解參數傳遞

不同的術語描述同一個概念：
- **Pass by Assignment** ← 最準確
- **Call by Object Reference** ← 也正確
- **Call by Sharing** ← 也正確

