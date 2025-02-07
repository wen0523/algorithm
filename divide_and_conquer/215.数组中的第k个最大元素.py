#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 基于快速排序(并使用双指针优化)
        def quickSort(nums, left = None, right = None):
            left = 0 if not isinstance(left,(float,int)) else left
            right = len(nums) - 1 if not isinstance(right,(float,int)) else right

            while left < right:
                index = getIndex(nums, left, right)
                if index + k == len(nums):
                    return nums[index]
                elif index + k > len(nums):
                    right = index - 1
                else:
                    left = index + 1

            return nums[left]

        # Lomuto 分区法 (i = left+1),适用于 小规模数据，但在 O(n²) 退化更严重,适用于标准 quicksort
        # def getIndex(nums, left, right):
        #     pivot = nums[left]  # 选取 pivot
        #     i, j = left, right
            
        #     # 先遍历j，防止过早跳过pivot
        #     while i < j:
        #         while i < j and nums[j] >= pivot:  # 右指针找到小于 pivot 的数
        #             j -= 1
        #         while i < j and nums[i] <= pivot:  # 左指针找到大于 pivot 的数
        #             i += 1
        #         if i < j:
        #             swap(nums, i, j)  # 交换不符合条件的元素

        #     swap(nums, left, j)  # 把 pivot 放到正确的位置
        #     return j

        # Hoare 分区法 (i = l-1, j = r+1)
        # 比 Lomuto 更稳定，更适合 数据分布不均 的情况,适合 quickselect，保证 O(n) 期望复杂度
        def getIndex(nums, left, right):
            pivot = nums[left]  # 选取最左端点为 pivot
            i = left - 1
            j = right + 1

            while True:
                # 找到左侧第一个 >= pivot 的数
                while True:
                    i += 1
                    if nums[i] >= pivot:
                        break

                # 找到右侧第一个 <= pivot 的数
                while True:
                    j -= 1
                    if nums[j] <= pivot:
                        break

                if i >= j:
                    return j  # `j` 是新的 pivot 位置

                # 交换 nums[i] 和 nums[j]
                nums[i], nums[j] = nums[j], nums[i]

        def swap(nums, i, index):
            nums[i],nums[index] = nums[index],nums[i]

        return quickSort(nums, 0, len(nums)-1)

# @lc code=end

