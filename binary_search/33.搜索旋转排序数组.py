#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(0,len(nums)):
        #     if(nums[i] == target):
        #         return i
            
        # return -1

        #二分
        area = ''
        if(len(nums) == 1 or nums[-1] > nums[0]):
            area=''
        elif(target <= nums[-1]):
            area = 'r'
        elif(target >= nums[0]):
            area = 'l'
        else:
            return -1
        
        i,j = 0,len(nums)-1
        l,r = nums[0],nums[-1]

        while i <= j:
            mid = (i+j)//2
            if(area == 'l' and nums[mid] <= r):
                j = mid - 1
            elif(area == 'r' and nums[mid] >= l):
                i = mid + 1
            else:
                if(target < nums[mid]):
                    j = mid - 1
                elif(target > nums[mid]):
                    i = mid + 1
                else:
                    return mid
                
        return -1

# @lc code=end

