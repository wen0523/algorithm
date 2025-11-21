#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第 K 小的元素
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def getList(root: Optional[TreeNode]):
            if root == None:
                return []
            
            res = []

            res.append(root.val)
            res+= getList(root.left)
            res+= getList(root.right)

            return res
        
        res = getList(root)

        for i in range(0, len(res) - 1):
            isSwap = False
            if i == k:
                return res[len(res) - k]
            for j in range(0, len(res)-1):
                if res[j] < res [j+1]:
                    res[j+1],res[j] = res[j],res[j+1]
                    isSwap = True

            if not isSwap:
                return res[len(res) - k]
            
        return res[len(res) - k]
# @lc code=end