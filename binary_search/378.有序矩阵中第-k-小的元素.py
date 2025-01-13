#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第 K 小的元素
#

# @lc code=start
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def getCount(mid):
            i,j = n-1,1
            count = 0

            while i>=0:
                while True:
                    if j == n-1 and matrix[i][j] <= mid:
                        return count+(i+1)*n
                    elif matrix[i][j] <= mid:
                        j = j + 1
                    else:
                        count = count + j
                        break
                i = i - 1
            
            return count
        
        l,r = matrix[0][0],matrix[-1][-1]

        while l<=r:
            mid = (l+r)//2
            count = getCount(mid)

            if count > k:
                r = mid - 1
            elif count < k:
                l = mid + 1
            else:
                return mid
            
        return r

# @lc code=end

