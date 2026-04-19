# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def rec( root ) :
            res = []
            if root.left is None and root.right is None : 
                return [root.val]
            else :
                if root.left is not None :
                    res.extend( rec( root.left ) ) 
                if root.right is not None :
                    res.extend( rec( root.right ) )
                return res
        return rec( root1 ) == rec( root2 )

        