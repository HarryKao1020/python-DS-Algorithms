import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # 虚拟头结点
        dummy = ListNode(-1)
        p = dummy
        p1 = list1
        p2 = list2

        while p1 is not None and p2 is not None:

            # 比较 p1 和 p2 两个指针
            # 将值较小的的节点接到 p 指针
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            # p 指针不断前进
            p = p.next

        if p1 is not None:
            p.next = p1

        if p2 is not None:
            p.next = p2

        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode.create_head([1, 2, 4])
    l2 = ListNode.create_head([1, 3, 4])

    res = solution.mergeTwoLists(l1, l2)
    ListNode.print(res)
