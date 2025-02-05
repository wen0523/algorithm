#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 直接方法(空间复杂度不符合)
        dict = {}
        lenth = len(nums)//2 + 1
        for i in nums:
            dict[i] = dict.get(i,0) + 1
            if dict[i] >= lenth:
                return i



# @lc code=end

