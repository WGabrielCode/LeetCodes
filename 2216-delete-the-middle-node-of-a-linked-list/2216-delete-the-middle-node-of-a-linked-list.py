# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        q = head
        size = 0
        while q is not None : 
            size += 1 
            q = q.next
        
        if size == 1 :
            return None

        idx = 0
        q = head 
        before = q
        while idx < size // 2 :
            before = q
            q = q.next
            idx += 1
        before.next = q.next 
        return head