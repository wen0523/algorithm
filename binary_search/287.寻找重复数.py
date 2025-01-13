#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i,j = 1,len(nums)-1
        while i <= j:
            mid = (i+j)//2
            cnt = 0
            for num in nums:
                if num<=mid:
                    cnt = cnt + 1
            
            if cnt <= mid:
                i = mid + 1
            else:
                j = mid - 1

        return i
        
# @lc code=end

