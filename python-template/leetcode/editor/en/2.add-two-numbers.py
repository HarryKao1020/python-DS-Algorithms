#
# @lc app=leetcode id=2 lang=python3
# @lcpr version=30201
#
# [2] Add Two Numbers
#
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        carry = 0
        dummy = ListNode(-1)  # 第三條list(結果)的頭
        p = dummy

        while p1 is not None or p2 is not None or carry > 0:
            val = carry
            if p1 is not None:
                val += p1.val
                p1 = p1.next
            if p2 is not None:
                val += p2.val
                p2 = p2.next

            carry = val // 10  # 如果相加是大於10, carry=1 如果是小於0,carry=0
            val = val % 10  # 相加假如是13 , val 會是3 , 如果是 7 , val就是7
            p.next = ListNode(val)
            p = p.next

        return dummy.next  # 返回虛擬頭的下一個節點就是答案


# @lc code=end


#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#
