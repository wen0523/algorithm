#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def getResult(nums, target):
            i,j = 0, len(nums)-1
            while i<=j:
                mid = (i+j)//2
                if nums[mid] > target:
                    j = mid - 1
                elif nums[mid] < target:
                    i = mid + 1
                else:
                    return True
            
            return j
        
        new_nums = []
        for items in matrix:
            new_nums.append(items[0])

        col_i,col_j = 1, getResult(matrix[0], target)
        row_i,row_j = 1, getResult(new_nums, target)

        if (isinstance(row_j,bool) or isinstance(col_j,bool)):
            return True
        
        for i in range(row_i,row_j+1):
            nums = matrix[i][col_i:col_j+1]

            result = getResult(nums, target)

            if isinstance(result,bool):
                return True
            
        return False
        
# @lc code=end

