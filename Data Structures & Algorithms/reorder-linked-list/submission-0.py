# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list_arr =  []
        curr = head
        
        while curr:
            list_arr.append(curr)
            curr = curr.next

        l,r = 0, len(list_arr) - 1
        while l < r:
            list_arr[l].next = list_arr[r]
            l += 1

            if l == r:
                break
            
            list_arr[r].next = list_arr[l]
            r -= 1

        list_arr[l].next = None
        
