#
# @lc app=leetcode.cn id=719 lang=python3
#
# [719] 找出第 K 小的数对距离
#

# @lc code=start
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def count(mid: int) -> int:
            count = 0
            j = 0
            n = len(nums)
            for i in range(n):
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1

                count += j - i - 1

            return count

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            if count(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left


# @lc code=end
