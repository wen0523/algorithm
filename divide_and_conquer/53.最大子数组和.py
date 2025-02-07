#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        动态规划
        规划转移方程：
        f(i)=max{f(i−1)+nums[i],nums[i]}
        '''

        # pre = 0
        # max_ans = nums[0]
        # for i in nums:
        #     pre = max(pre + i, i)
        #     max_ans = max(max_ans, pre)
            
        # return max_ans

        '''
        分治
        对于一个区间 [l,r]，我们可以维护四个量：

        lSum 表示 [l,r] 内以 l 为左端点的最大子段和
        rSum 表示 [l,r] 内以 r 为右端点的最大子段和
        mSum 表示 [l,r] 内的最大子段和
        iSum 表示 [l,r] 的区间和

        以下简称 [l,m] 为 [l,r] 的「左子区间」，[m+1,r] 为 [l,r] 的「右子区间」。我们考虑如何维护这些量呢（如何通过左右子区间的信息合并得到 [l,r] 的信息）？对于长度为 1 的区间 [i,i]，四个量的值都和 nums[i] 相等。对于长度大于 1 的区间：
        首先最好维护的是 iSum，区间 [l,r] 的 iSum 就等于「左子区间」的 iSum 加上「右子区间」的 iSum。
        对于 [l,r] 的 lSum，存在两种可能，它要么等于「左子区间」的 lSum，要么等于「左子区间」的 iSum 加上「右子区间」的 lSum，二者取大。
        对于 [l,r] 的 rSum，同理，它要么等于「右子区间」的 rSum，要么等于「右子区间」的 iSum 加上「左子区间」的 rSum，二者取大。
        当计算好上面的三个量之后，就很好计算 [l,r] 的 mSum 了。我们可以考虑 [l,r] 的 mSum 对应的区间是否跨越 m——它可能不跨越 m，也就是说 [l,r] 的 mSum 可能是「左子区间」的 mSum 和 「右子区间」的 mSum 中的一个；它也可能跨越 m，可能是「左子区间」的 rSum 和 「右子区间」的 lSum 求和。三者取大。
        '''
        
        # iSum,lSum,rSum,mSum
        def getinfo(lnums, rnums):
            iSum = lnums[0] + rnums[0]
            lSum = max(lnums[1], lnums[0] + rnums[1])
            rSum = max(rnums[2], rnums[0] + lnums[2])
            mSum = max(lnums[3], rnums[3], lnums[2] + rnums[1])

            return [iSum,lSum,rSum,mSum]

        def divideAndConquer(l, r):
            if l == r:
                num = nums[l]
                return [num]*4

            mid = (l + r)//2
            left = divideAndConquer(l, mid)
            right = divideAndConquer(mid + 1, r)

            return getinfo(left, right)

        return divideAndConquer(0, len(nums) - 1)[3]            
# @lc code=end

