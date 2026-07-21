# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head = ListNode(None)
        curr = head

        while list1 and list2:
            if list1.val>list2.val:
                node = ListNode(list2.val)
                curr.next = node
                curr = curr.next
                list2 = list2.next
            else:
                node = ListNode(list1.val)
                curr.next = node
                curr = curr.next
                list1 = list1.next

        while list1:
            node = ListNode(list1.val)
            curr.next = node
            curr = curr.next
            list1 = list1.next
        while list2:
            node = ListNode(list2.val)
            curr.next = node
            curr = curr.next
            list2 = list2.next
        return head.next