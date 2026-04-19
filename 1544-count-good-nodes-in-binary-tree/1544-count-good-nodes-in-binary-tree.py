# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def rec( node, curr_max ):
            
            nonlocal result

            if node.val >= curr_max :
                result += 1
                curr_max = node.val

            if node.left is not None :
                rec( node.left, curr_max )

            if node.right is not None :
                rec( node.right, curr_max )

        result = 0
        rec( root , root.val )
        return result