# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def get_kth(curr,k):
            while curr and k>0:
                curr=curr.next
                k-=1
            
            return curr
        
        dummy = ListNode()
        dummy.next = head
        group_prev = dummy

        while True:
            kth = get_kth(group_prev,k)

            if not kth:
                break
            
            group_next = kth.next
            kth.next = None
            prev = None
            curr = group_prev.next
            tail = curr

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            group_prev.next = prev
            tail.next = group_next
            group_prev = tail
        
        return dummy.next

        