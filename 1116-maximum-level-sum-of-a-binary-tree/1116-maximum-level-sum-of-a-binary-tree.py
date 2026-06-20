# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0

        from collections import deque
        


        curr_lvl = 0

        max_sum = -float("inf")
        max_lvl = -1

        q = deque()
        q.append( root )

        while q :
            curr_lvl += 1
            lvl_size = len( q )
            lvl_sum = 0


            for _ in range( lvl_size ) :
                head = q.popleft()
                
                lvl_sum += head.val

                if head.left is not None :
                    q.append(head.left)
                if head.right is not None :
                    q.append(head.right)
                
            if lvl_sum > max_sum :
                max_sum = lvl_sum
                max_lvl = curr_lvl
        
        return max_lvl
        