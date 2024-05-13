"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        traversal = list()

        if root:
            for child in root.children:
                traversal+=self.postorder(child)

            traversal.append(root.val)

        return traversal