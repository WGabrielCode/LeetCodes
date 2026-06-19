# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        def rec( head, lvl ):
            if head is None :
                return 
            
            n = len( lvl_sum )
            if n <= lvl :
                lvl_sum.append( head.val )
            else :
                lvl_sum[lvl] += head.val
            rec(head.left , lvl+1 )
            rec(head.right , lvl+1 )

        lvl_sum = []
        
        rec( root , 0 )

        max_sum = -float('inf')
        max_lvl = None
        for idx, val in enumerate( lvl_sum ) :
            if val > max_sum :
                max_sum = val
                max_lvl = idx

        return max_lvl + 1
        