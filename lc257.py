# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        path=""
        res=[]

        def dfs(node,path):

            if node is None:
                return 
            
            if node.left is None and node.right is None:
                new_path = path + str(node.val)
                res.append(new_path)
                return

            new_path = path + str(node.val) + "->"

            dfs(node.left,new_path)
            dfs(node.right,new_path)
        
        dfs(root,path)
        return res