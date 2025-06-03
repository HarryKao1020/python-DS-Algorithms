#
# @lc app=leetcode id=1 lang=python3
# @lcpr version=30201
#
# [1] Two Sum
#
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for index, value in enumerate(nums):
            x = target - value
            if value in ht:
                return [ht[value], index]
            ht[x] = index
        return []


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    l1 = [3, 3]

    res = solution.twoSum(l1, 6)

    print(res)


#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#
