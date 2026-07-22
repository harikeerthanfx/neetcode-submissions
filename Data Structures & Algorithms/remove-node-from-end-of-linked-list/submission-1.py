# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        if length == 1:
            return None

        index = length - n + 1 #one indexed

        if index == 1:
            return head.next

        curr = head
        prev = ListNode()
        i = 1
        while i < index:
            print(i)
            prev = curr
            curr = curr.next
            i += 1
        
        prev.next = curr.next
        return head
