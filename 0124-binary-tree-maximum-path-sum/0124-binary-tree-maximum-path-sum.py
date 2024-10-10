# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(root):
            if not root: return 0
            leftMax = max(0, dfs(root.left))
            rightMax = max(0, dfs(root.right))
            
            res[0] = max(root.val + leftMax + rightMax, res[0])
            return root.val + max(rightMax, leftMax)
        dfs(root)
        return res[0]