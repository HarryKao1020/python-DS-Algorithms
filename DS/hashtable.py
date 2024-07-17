class Node:
    def __init__(self, key, value=None):
        self.next = None
        self.key = key
        self.value = value


class HashTable:

    # 初始化哈希表，默認大小為 10。使用一個列表來存儲每個桶，每個桶初始為 None。
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    # hash function 是用來把key用hash function雜湊加密成一個Hashed Text當作索引,
    # 並將value放入與索引連結的bucket內
    def hash_function(self, key):
        return hash(key) % self.size

    # 新增一組key , value ,如果鍵已存在，則更新其值。否則，將新節點添加到鏈表的末尾。
    def put(self, key, value):
        # 透過hash function 產生一個index , index< m(10)
        index = self.hash_function(key)
        print("index:", index)
        new_node = Node(key, value)
        current_node = self.table[index]

        if current_node is None:
            self.table[index] = new_node
        else:
            prev_node = None
            while current_node:
                if current_node.key == key:
                    current_node.value = value
                    return
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = new_node

    def get(self, key):
        index = self.hash_function(key)
        print("get index:", index)
        current_node = self.table[index]
        while current_node:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
            print("current_node", current_node.key)
        return None

    def remove(self, key):
        index = self.hash_function(key)
        current_node = self.table[index]
        prev_node = None

        while current_node:
            if current_node.key == key:
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    self.table[index] = current_node.next
                return True
            prev_node = current_node
            current_node = current_node.next
        return False

    def __repr__(self):
        items = []
        for index in range(self.size):
            current_node = self.table[index]
            while current_node:
                items.append(f"{current_node.key}:{current_node.value}")
                current_node = current_node.next
        return "{" + ", ".join(items) + "}"


ht = HashTable()
ht.put("one", 1)
ht.put("two", 2)
ht.put("three", 3)
ht.put("four", 4)
ht.put("five", 5)
ht.remove("three")
print(ht.get("one"))


print("Hash Table", ht)
