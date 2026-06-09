# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def calculate_num(l):
            curr1 = l
            num1 = 0
            i=0

            while curr1:
                num1 = curr1.val*10**i + num1
                i+=1
                curr1 = curr1.next
            
            return num1
        
        sum = calculate_num(l1) + calculate_num(l2)

        if sum==0:
            return ListNode(0)

        head = ListNode()

        curr = head

        while sum>0:
            n=sum%10
            curr.next = ListNode(n)
            curr = curr.next
            sum=sum//10

        return head.next
        