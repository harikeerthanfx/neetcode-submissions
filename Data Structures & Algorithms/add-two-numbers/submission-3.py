# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0

        while l1 or l2 or not carry == 0:
            v1 = l1.val if not l1 == None else 0
            v2 = l2.val if not l2 == None else 0
            
            sum = v2 + v1 + carry
            digit = sum%10
            curr.next = ListNode(digit)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
            carry = sum//10
        return dummy.next
        


