# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avgs=[]
        queue=deque()
        queue.append(root)

        while queue:
            avg=0
            n=len(queue)

            for _ in range(n):
                node=queue.popleft()
                avg+=node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            avg/=n
            avgs.append(avg)

        return avgs
