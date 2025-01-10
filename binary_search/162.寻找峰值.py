#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #    return 0
        # else:
        #     if nums[0] > nums[1]:
        #         return 0
        #     elif nums[-1] > nums[-2]:
        #         return len(nums) - 1
        #     else:
        #         i = 1
        #         while i <= len(nums)-2:
        #             if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        #                 return i 
                    
        #             i = i+1

        #二分方法
        i,j = 0,len(nums)-1
        mid = 0

        while j-i>=2:
            mid = (i+j)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                i = mid + 1
            else:
                j = mid - 1
        
        if j-i == 0:
            return i
        elif j-i == 1:
            return i if nums[i] > nums[j] else j


            
# @lc code=end

