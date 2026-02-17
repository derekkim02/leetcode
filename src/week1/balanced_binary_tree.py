# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        if root == None:
            return True
        
        self.is_balanced = True
        def dfs(tree):
            if tree == None:
                return 0
            
            l_height = dfs(tree.left)
            r_height = dfs(tree.right)

            if abs(l_height - r_height) > 1 :
                self.is_balanced = False

            return max(l_height, r_height) + 1
        
        dfs(root)