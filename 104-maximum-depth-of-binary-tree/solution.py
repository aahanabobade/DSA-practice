# Maximum Depth of Binary Tree
# Difficulty: Easy
# Runtime: 4 ms
# Memory: 15 MB
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        leftd = self.maxDepth(root.left)
        rightd = self.maxDepth(root.right)


        return 1 + max(leftd, rightd)
        
