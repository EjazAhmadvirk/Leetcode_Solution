# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        '''
            for reverse 1->2->3->4->5, process is like
                1->None, 2->3->4->5
                2->1->None, 3->4->5
                3->2->1->None, 4->5
                4->3->2->1->None, 5
                5->4->3->2->1->None, None
        '''
        def reverseList(head):
            pre, p = None, head
            while p:
                pnext = p.next
                p.next = pre
                pre = p
                p = pnext
            return pre

        dummy = ListNode(next=head)
        pre = cur = dummy
        while cur.next:
            for _ in range(k):
                cur = cur.next
                if cur is None:
                    return dummy.next
            t = cur.next
            cur.next = None # cut from next k-group, so to reverseList() for current k-group
            start = pre.next
            pre.next = reverseList(start)
            start.next = t # so now 'start' is the last node of k-group
            pre = cur = start # same as the reset dummy before while loop
        return dummy.next