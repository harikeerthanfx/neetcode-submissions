# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        curr = head
        if not curr:
            return False
        
        while curr:
            if curr in visited:
                return True
            else:
                visited.add(curr)
            curr = curr.next
        
        return False