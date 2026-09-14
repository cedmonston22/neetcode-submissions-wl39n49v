# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ll_len = 0
        curr = head
        while curr:
            ll_len += 1
            curr = curr.next
        
        to_remove = ll_len - n

        if to_remove == 0:
            return head.next

        curr = head

        for i in range(to_remove - 1):
            curr = curr.next

        curr.next = curr.next.next
        return head