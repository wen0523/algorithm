#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        
        def binary(num,bool = False):
            i,j = 0,len(nums)-1
            while i<=j:
                mid = (i+j)//2
                if(nums[mid]<num):
                    i = mid + 1
                else:
                    j = mid - 1

            if bool:
                return i
            else:
                return i if i<=len(nums)-1 and nums[i] == target else -1
        
        l = binary(target)
        if(l == -1):
            return [-1,-1]
        else:
            return [l,binary(target+1,bool=True)-1]

# @lc code=end

