#
# @lc app=leetcode id=151 lang=python3
# @lcpr version=30201
#
# [151] Reverse Words in a String
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        sb = []
        # 去除空格
        for c in s:
            if c != " ":
                # sb加入單字
                sb.append(c)
            elif sb and sb[-1] != " ":
                # 單字中間保留空格
                sb.append(" ")
        if not sb:
            return ""

        if sb[-1] == " ":
            sb.pop()

        # 去除空格的字串
        chars = list("".join(sb))
        n = len(chars)

        # 進行單詞的翻轉,先整體翻轉
        self.reverse(chars, 0, n - 1)

        i = 0
        while i < n:
            for j in range(i, n):
                if j + 1 == n or chars[j + 1] == " ":
                    self.reverse(chars, i, j)
                    i = j + 2
                    break
        return "".join(chars)

    # 翻轉 arr[i..j]
    def reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]  # 交換
            i += 1
            j -= 1


# @lc code=end


#
# @lcpr case=start
# "the sky is blue"\n
# @lcpr case=end

# @lcpr case=start
# "  hello world  "\n
# @lcpr case=end

# @lcpr case=start
# "a good   example"\n
# @lcpr case=end

if __name__ == "__main__":
    solution = Solution()
    test_word = "the sky is blue"

    res = solution.reverseWords(test_word)

    def reverse_word(word) -> str:
        return " ".join(reversed(word.split()))

    ans = reverse_word(test_word)
    type(ans)
    print(f"ANS:{ans}")
