# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        st = set()

        curr = head

        while curr:
            if curr in st:
                return True
            
            st.add(curr)
            curr = curr.next
        
        return False
        