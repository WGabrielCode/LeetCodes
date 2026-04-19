# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        values = []
        while head is not None :
            values.append(head.val)
            head = head.next
        
        result = 0
        for idx in range(len(values)//2) :
            current_sum = values[idx] + values[-(idx+1)]
            if current_sum > result :
                result = current_sum
        
        return result 
        
         