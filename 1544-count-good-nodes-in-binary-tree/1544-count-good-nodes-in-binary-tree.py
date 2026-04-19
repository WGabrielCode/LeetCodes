# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def rec( node, curr_max ):
            
            res = 0

            if node.val >= curr_max :
                res += 1
                curr_max = node.val

            if node.left is not None :
                res += rec( node.left, curr_max )

            if node.right is not None :
                res += rec( node.right, curr_max )
            return res 

        return rec( root , root.val )