class singleNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class singleLinkedList:

    # init , setting node head and next
    def __init__(self):
        self.head = None
        self.next = None

    # append to the last node
    def append(self, value):
        # setting new node
        new_node = singleNode(value)

        # If linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # if liked list have another data
        else:
            self.tail.next = new_node  # the list tail next is new node
            self.tail = self.tail.next  # the new node became the list tail

    # insert node in list
    def insert(self, index, value):

        # if list is empty , can't insert data
        if self.head is None:
            print("You can only insert the data to a not empty list")
        # if you want to insert node in head
        elif index == 0:
            new_node = singleNode(value)  # setting new node
            new_node.next = self.head  # new node next = origin list head
            self.head = new_node  # list head became new node

        # if you want to insert node in another index
        else:
            current = self.head
            new_node = singleNode(value)
            current_index = 0  # setting index begin from 0
            while (
                current_index + 1 < index and current.next is not None
            ):  # +1是因為他不會插入第0個了,會從1開始insert
                current = current.next  # current 跑到下一個
                current_index += 1  # index也要順便+1
            # 到達要插入的位置
            new_node.next = (
                current.next
            )  # 先把原本list 的current.next改到new node的next
            current.next = new_node  # 再把current.next 接到new node

            if new_node.next is None:  # setting list tail
                self.tail = new_node

    # remove method
    def remove(self, index):
        current_index = 0
        current = self.head
        if self.head is None:
            print("Is the empty list , can't remove data")
        elif index == 0 and self.length() > 1:  ## 刪除第一個值
            self.head = self.head.next

        # 刪除index大於0的
        while (
            current_index < index - 1 and current.next is not None
        ):  # 迴圈跑到要刪除的前一個
            current = current.next
            current_index += 1
        if current.next is None:
            print("超出索引值")

        current.next = current.next.next  # 要刪除的前一個的下一個指令的下下個

        if current.next is None:
            self.tail = current

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count


# sll = singleLinkedList()
# sll.append(1)
# sll.append(2)
# sll.append(3)
# sll.append(4)
# sll.insert(4, 20)
# sll.remove(4)
# sll.display()

# ============= Doubly


class DoubleNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoubleNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, value):
        new_node = DoubleNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, index):
        current_index = 0
        current = self.head
        while current_index < index - 1:
            current = current.next
            current_index += 1

        current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


dll = DoublyLinkedList()
for i in range(21):
    if i % 2 == 0:
        dll.append(i)

dll.display()
