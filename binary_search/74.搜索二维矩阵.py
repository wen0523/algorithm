#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #o(m*n)
        # for i in matrix:
        #     for j in i:
        #         if j == target:
        #             return True
                
        # return False
        
        #二分
        # def binary(nums):
        #     i,j = 0,len(nums)-1
        #     while i<=j:
        #         mid = (i+j)//2
        #         if nums[mid] < target:
        #             i = mid + 1
        #         elif nums[mid] > target:
        #             j = mid - 1
        #         else:
        #             return True
        #     return False
        
        # for items in matrix:
        #     if target <= items[-1]:
        #         return binary(items)
        
        # return False
        #优化二分
        m,n = len(matrix),len(matrix[0])
        min,max = 0,m*n-1
        while min <= max:
            mid = (max - min)//2 + min
            item = matrix[mid//n][mid%n]
            if item > target:
                max = mid - 1
            elif item < target:
                min = mid + 1
            else:
                return True
        return False
# @lc code=end

