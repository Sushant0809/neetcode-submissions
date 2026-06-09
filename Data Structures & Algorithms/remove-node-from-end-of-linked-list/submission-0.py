# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        l= 0 
        curr = head

        while curr:
            l+=1
            curr = curr.next
        
        node_rem = l-n

        if node_rem == 0:
            return head.next
        
        curr = head
        i = 0

        while curr:
            i+=1
            if i==node_rem:
                curr.next = curr.next.next
            curr = curr.next

        return head
        


        