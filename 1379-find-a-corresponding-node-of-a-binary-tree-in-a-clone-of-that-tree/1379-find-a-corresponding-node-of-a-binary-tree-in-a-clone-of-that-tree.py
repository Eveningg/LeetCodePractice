# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        # If either the original or cloned node is None, return None
        if original is None or cloned is None:
            return None

        # Check if the current node's value in the original tree matches the target value
        if original.val == target.val:
            # If it matches, return the current node from the cloned tree
            return cloned

        # Recursively search in the left subtrees of both trees
        left = self.getTargetCopy(original.left, cloned.left, target)
        # If a match is found in the left subtree, return it
        if left is not None:
            return left

        # Recursively search in the right subtrees of both trees
        right = self.getTargetCopy(original.right, cloned.right, target)
        # Return the result of the search in the right subtree
        return right