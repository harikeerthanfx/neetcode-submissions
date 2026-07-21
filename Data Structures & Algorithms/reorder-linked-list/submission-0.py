# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse from slow.next till the end and start adding to the first half
        node = self.reverseList(slow.next)
        slow.next = None

        rightlist = node
        l = head
        while rightlist:
            temp = l.next
            l.next = rightlist
            temp2 = rightlist.next
            rightlist.next = temp
            l = rightlist.next
            rightlist = temp2



    def reverseList(self,node):
        prev = None
        curr = node
         
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
            

        
