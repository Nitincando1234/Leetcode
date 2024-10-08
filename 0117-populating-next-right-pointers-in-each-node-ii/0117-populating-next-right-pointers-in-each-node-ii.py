"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # BFS based solution
        if not root:
            return root
        queue = deque([root])
        while queue:
            pre = None
            for _ in range(len(queue)):
                cur = queue.popleft()
                if pre: pre.next = cur
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
                pre = cur
        return root