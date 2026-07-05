class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def rec( head ) :
            
            left , right = None , None
            if head.left is not None :
                left = rec( head.left ) 

            if head.right is not None :
                right = rec( head.right )
            
            l_type = isinstance( left , TreeNode ) 
            r_type = isinstance( right, TreeNode )

            current = True if head is p or head is q else False 
            if current and (l_type or r_type) :
                return head
            if l_type and r_type:
                return head
            if l_type :
                return left
            if r_type :
                return right
        

            if head is p or head is q :
                return head 

        found_flag = False 
        return rec( root )
        
