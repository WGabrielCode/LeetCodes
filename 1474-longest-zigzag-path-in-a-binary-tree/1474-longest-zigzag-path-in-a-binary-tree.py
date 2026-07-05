# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # dir( 0 - left, 1-right )
        def rec( head ) :
            
            left = rec( head.left )[1] if head.left is not None else 0
            right = rec( head.right )[0] if head.right is not None else 0

            m = max( left, right ) 
            nonlocal max_path
            if m > max_path : 
                max_path = m 

            return (left + 1 ,right + 1)
            

        max_path = 0

        rec( root )

        return max_path