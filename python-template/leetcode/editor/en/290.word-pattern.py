#
# @lc app=leetcode id=290 lang=python3
# @lcpr version=30201
#
# [290] Word Pattern
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_list = list(pattern)
        s_list = s.split(" ")
        print(p_list)
        print(s_list)
        if len(p_list) != len(s_list):
            return False
        pattern_to_word = {}
        word_set = set()
        for i, c in enumerate(p_list):
            print(f"i:{i} , c:{c}")
            word = s_list[i]
            if c not in pattern_to_word:
                if word in word_set:
                    return False
        return True


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    pattern = "abba"
    s = "dog cat cat dog"

    res = solution.wordPattern(pattern, s)

    print(res)


#
# @lcpr case=start
# "abba"\n"dog cat cat dog"\n
# @lcpr case=end

# @lcpr case=start
# "abba"\n"dog cat cat fish"\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n"dog cat cat dog"\n
# @lcpr case=end
