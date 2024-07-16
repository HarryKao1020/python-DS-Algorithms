## Stack - LIFO (Last in ,First Out)


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        else:
            poped_node = self.top
            self.top = self.top.next
            self._size -= 1
            return poped_node.value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        else:
            return self.top.value

    def size(self):
        return self._size


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())
print(s1.pop())
print(s1.size())
s1.push(40)
print(s1.peek())
