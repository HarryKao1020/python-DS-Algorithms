#
# @lc app=leetcode id=141 lang=python3
# @lcpr version=30201
#
# [141] Linked List Cycle
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # 快指針走到尾停止,如果是環就不會停止
        while fast is not None and fast.next is not None:
            # 快指針走2步,慢指針走1步
            slow = slow.next
            fast = fast.next.next
            # 快慢指針相遇 確定有環,但相遇的點不是尾巴接的點
            if slow == fast:
                return True

        return False


# @lc code=end


#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#
