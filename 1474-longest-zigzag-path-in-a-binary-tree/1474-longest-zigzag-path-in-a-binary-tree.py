# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # dir( 0 - left, 1-right )
        def rec( head , dir : bool, sum:int ) :
            sum += 1

            
            left_dir = dir if dir else not dir
            right_dir = not left_dir
            
            left_sum = 0 if dir else sum 
            right_sum = sum if dir else 0
            
            result = sum 
            if head.left is not None :
                result = max( result, rec( head.left ,left_dir, left_sum ) ) 
            if head.right is not None :
                result = max( result,  rec( head.right, right_dir, right_sum) ) 

            return result
                               
        return max( rec( root , 0 ,  -1 ), rec(root, 1, -1 ) ) 
