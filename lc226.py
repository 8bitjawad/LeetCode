# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def backtrack(root):
            if root == None:
                return

            root.left,root.right= root.right,root.left
            backtrack(root.left) and backtrack(root.right)


        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def backtrack(root):
            if root == None:
                return

            root.left,root.right= root.right,root.left
            backtrack(root.left)
            backtrack(root.right)

            return root


        backtrack(root)

        return root



        