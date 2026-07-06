class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None :
            return None 
        if root.val == key :
            if root.left :
                head = root.left
                left_head = root.left
                if root.right :
                    while left_head.right :
                        left_head = left_head.right
                    left_head.right = root.right
                return head
            return root.right


        prev = root
        head = root 
        while head.val != key :
            prev = head
            if head.val < key :
                head = head.right
            else :
                head = head.left 
            if head is None :
                return root
        

        if head.left :
            result = head.left 
            left_head = head.left
            if head.right :
                while left_head.right :
                    left_head = left_head.right
                left_head.right = head.right
        else :
            result = head.right


        if prev.left is head :
            prev.left = result
        else :
            prev.right = result
        

        return root 