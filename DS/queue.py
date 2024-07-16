## Queue is FIFO (First in First out)
# 特性：
# 有兩個端點，分為前端與後端
# 後端只可新增資料
# 前端只可刪除與讀取資料
# 資料的存取必須符合先進先出(First In First Out, FIFO)


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        else:
            remove_node = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            self._size -= 1
            return remove_node.value

    def peek(self):
        if self.is_empty():
            raise IndexError("empty queue")
        else:
            return self.front.value

    def size(self):
        return self._size


q1 = Queue()
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(80)
print(q1.size())
print(q1.dequeue())
print(q1.dequeue())
print(q1.peek())
