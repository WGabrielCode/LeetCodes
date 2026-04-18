# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd = head

        if odd.next is None:
            return head

        even_head = head.next
        even = even_head

        idx = 0
        while odd is not None and even is not None:
            if idx & 1:
                even.next = odd.next
                even = even.next
            else:
                odd.next = even.next
                if even.next is None:
                    break
                odd = odd.next
            idx += 1

        odd.next = even_head
        return head