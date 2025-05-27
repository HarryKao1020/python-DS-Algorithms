#
# @lc app=leetcode id=283 lang=python3
# @lcpr version=30201
#
# [283] Move Zeroes
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = self.removeElement(nums, 0)

        for i in range(p, len(nums)):
            nums[i] = 0

    def removeElement(self, nums: List[int], val: int) -> int:
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


# @lc code=end


#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

if __name__ == "__main__":
    solution = Solution()
    l1 = [1, 2, 0, 4, 0, 3]

    res = solution.moveZeroes(l1)

    print(res)
