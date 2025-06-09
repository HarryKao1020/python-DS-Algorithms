import sys

from typing import List, Dict, Set, Tuple

# ======
# python 是 『pass by value』 還是 『pass by reference』 ?
#
#
# ======

# 基本型別 - Reference
name: str = "Harry"  #
age: int = 26
height: float = 173.5
is_jobber: bool = True
gender: str
gender = "male"

# 要import List, Dict, Set, Tuple
numbers: List[int] = [1, 2, 3, 4, 5]
grades: Dict[str, int] = {"math": 90, "english": 86}
tags: Set[str] = {"python", "java"}
coordinate: Tuple[float, float] = (10.5, 20.3)

print(f"numbers:{numbers}")

# 檢查物件記憶體大小
print(sys.getsizeof(name))
print(f"記憶體位置:{id(name)}")  # 記憶體位置

# 檢查型別
print(type(name))
print(isinstance(name, str))  # --> return True or False
