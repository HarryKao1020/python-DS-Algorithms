#
# @lc app=leetcode id=142 lang=python3
# @lcpr version=30201
#
# [142] Linked List Cycle II
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if not fast or not fast.next:
            return None

        # fast slow相遇後,把其中一個指向head
        slow = head

        # 快慢指針開始同步前進,再次相遇的點就是環的起點
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


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
