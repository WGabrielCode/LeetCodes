class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        from collections import deque

        reverse_path = deque()
        reverse_p  = None 
        reverse_q = None 
    
        def rec( head ) :
            nonlocal reverse_p , reverse_q, reverse_path
            if not ( reverse_p is None ) and not ( reverse_q is None ) :
                return 
            
            reverse_path.append( head )

            if head is p :
                reverse_p = reverse_path.copy()
            elif head is q :
                reverse_q = reverse_path.copy()
                

            if head.left is not None :
                rec( head.left ) 
                if reverse_path : 
                    reverse_path.pop()
            if head.right is not None :
                rec( head.right )
                if reverse_path :
                    reverse_path.pop()
    
        rec( root ) 

        while len( reverse_q ) > len( reverse_p ) :
            reverse_q.pop()
        while len( reverse_p ) > len( reverse_q ) :
            reverse_p.pop()

        while reverse_p :
            p = reverse_p.pop()
            q = reverse_q.pop() 
            if p is q :
                return p

        return None 

        
