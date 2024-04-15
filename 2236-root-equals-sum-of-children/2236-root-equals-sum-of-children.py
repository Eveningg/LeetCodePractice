# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:

        # checking root value has a value
        if root != None:
            
            if root.val == root.left.val + root.right.val:
                return True
            
            else:
                return False
        
        else:
            return False