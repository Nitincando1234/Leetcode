# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        largest_values = []
        queue = collections.deque([root])
        while queue:
            max_seen = float("-inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                max_seen = max(node.val, max_seen)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            largest_values.append(max_seen)
        return largest_values