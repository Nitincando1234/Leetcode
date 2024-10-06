# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #   Three method to solve:
        #   recursive dfs method
        #   iterative dfs method
        #   bfs method
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        