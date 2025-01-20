#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #快速幂
        negative = False
        if n == 0:
            return 1
        if n < 0:
            n = -n
            negative = True

        result = x
        ans = 1

        while n>0:
            if n%2 == 1:
                ans = ans*result
        
            result = result * result
            n = n//2
        
        return 1/ans if negative else ans
        
# @lc code=end

