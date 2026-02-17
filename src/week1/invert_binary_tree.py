# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        def invert(start):
            if start == None:
                return
            left = start.left
            start.left = start.right
            start.right = left

            invert(start.left)
            invert(start.right)
        
        invert(root)
        return root