#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # minNum = nums[left]

        # while left <= right:
        #     # if left == len(nums) - 1:
        #     #     return nums[left]
        #     mid = (left + right) // 2
        #     minNum = min(minNum, nums[mid])

        #     # 找出最小值所在位置
        #     if nums[left] < nums[mid]:
        #         # 说明在右侧
        #         minNum = min(minNum, nums[left])
        #         left = mid + 1
        #     else:
        #         minNum = min(minNum, nums[right])
        #         # 说明在左侧
        #         right = mid - 1

        # return minNum

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


# @lc code=end
