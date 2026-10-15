# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        shead = ListNode(val=head.val)
        curr = head.next
        while curr:
            nnode = ListNode(curr.val)
            currs = shead
            prev = None
            while currs:
                if nnode.val < currs.val:
                    if prev:
                        prev.next = nnode
                    else:
                        shead = nnode
                    nnode.next = currs
                    break
                if currs.next:
                    prev = currs
                    currs = currs.next
                else:
                    currs.next = nnode
                    break
            curr = curr.next
        return shead
            