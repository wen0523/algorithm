#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # if target in nums:
        #     return True
        # else:
        #     return False

        # 二分查找
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # 无法判断那边有序
            if nums[left] == nums[mid] == nums[right - 1]:
                left += 1
                right -= 1
                continue

            # 左侧有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right - 1]:
                    left = mid + 1
                else:
                    right = mid

        return False


# @lc code=end
