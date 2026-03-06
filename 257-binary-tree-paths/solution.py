# Binary Tree Paths
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/binary-tree-paths/

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        
        def dfs(node, path):
            if not node:
                return
            
            path += str(node.val)
            
            # if leaf node
            if not node.left and not node.right:
                res.append(path)
                return
            
