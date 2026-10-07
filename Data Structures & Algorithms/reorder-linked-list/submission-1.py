# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node_list = []
        curr = head

        while curr:
            node_list.append(curr)
            curr = curr.next
        
        l, r = 0, len(node_list) - 1
        while l < r:
            node_list[l].next = node_list[r]
            l += 1

            if l == r:
                break
            
            node_list[r].next = node_list[l]
            r -=  1
        node_list[l].next = None

        #test [1,4,5,7,8,9]
        #output [1,9,4,8,5,7]