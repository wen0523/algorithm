#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        target = x
        min,max = 0,x
        mid = 0
        while min <= max:
            mid = min + (max - min)//2
            if mid*mid == target:
                return mid
            elif mid*mid < target:
                min = mid + 1
            else:
                max = mid -1
        
        return max

# @lc code=end

