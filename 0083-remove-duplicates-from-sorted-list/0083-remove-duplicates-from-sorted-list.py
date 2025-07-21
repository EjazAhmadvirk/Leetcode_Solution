# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        
        while current is not None and current.next is not None:
            if current.val == current.next.val:
                temp = current.next
                current.next = current.next.next
                del temp  # Optional in Python, as garbage collection handles it
            else:
                current = current.next
        
        return head
     