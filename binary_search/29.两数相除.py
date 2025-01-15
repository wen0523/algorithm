#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        #一些特殊情况
        if(divisor == INT_MIN):
            if(dividend == INT_MIN):
                return 1
            else:
                return 0

        if(divisor == INT_MAX):
            if(dividend == INT_MIN or dividend == -INT_MAX):
                return -1
            if(dividend == INT_MAX):
                return 1
            
            return 0

        if(dividend == INT_MIN):
            if(divisor == 1):
                return INT_MIN
            if(divisor == -1):
                return INT_MAX
            
        if(dividend == 0):
            return 0
        
        #正常情况
        bool = False

        if(dividend > 0):
            dividend = -dividend
            bool = not bool

        if(divisor > 0):
            divisor = -divisor
            bool = not bool

        def getResult(a,b):
            result = 0
            
            while b > 0:
                if b&1:
                    result = result + a

                a<<=1
                b>>=1
            
            return result
        
        min,max = 1,INT_MAX
        while min<=max:
            mid = min + (max - min)//2
            result = getResult(-divisor,mid)
            if result > -dividend:
                max = mid - 1
            else:
                min = mid + 1

        if(bool):
            max = -max
        
        return max
# @lc code=end

