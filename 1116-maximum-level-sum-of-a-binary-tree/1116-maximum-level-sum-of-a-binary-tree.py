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
        
        last_lvl = 1
        last_sum = 0

        max_sum = -float("inf")
        max_lvl = -1

        q = deque()
        q.append( (root,1) )

        while q :
            (head, curr_lvl) = q.popleft()
            if last_lvl < curr_lvl:
                if last_sum > max_sum :
                    max_sum = last_sum 
                    max_lvl = last_lvl

                last_lvl = curr_lvl
                last_sum = head.val
            else :
                last_sum += head.val

            if not (head.left is None) :
                q.append( (head.left,curr_lvl+1 ) )
            if not (head.right is None ):
                q.append( (head.right,curr_lvl+1 ) )
        if max_sum < last_sum :
            max_lvl = last_lvl
        return max_lvl
        