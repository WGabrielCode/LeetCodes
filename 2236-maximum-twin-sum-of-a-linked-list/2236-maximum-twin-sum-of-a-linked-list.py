# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        if head.next.next is None :
            return head.val + head.next.val
         
        prev = None 
        curr = head 
        next = None 
        quick_curr = head

        while quick_curr is not None and quick_curr.next is not None: 
            quick_curr = quick_curr.next.next
            next, curr.next, prev = curr.next, prev, curr
            curr = next 

        left = prev
        right = curr
        result = 0

        while left is not None : 
            curr_sum = left.val + right.val 
            if curr_sum > result :
                result = curr_sum
            left = left.next 
            right = right.next
        
        return result
        
         