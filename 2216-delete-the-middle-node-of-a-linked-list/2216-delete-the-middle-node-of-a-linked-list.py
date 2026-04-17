# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is not None and head.next is None :
            return None
        
        quick = head
        slow = head 
        before = head 
        

        while quick is not None and quick.next is not None :
            quick = quick.next.next
            before = slow 
            slow = slow.next

        before.next = slow.next

        return head 

