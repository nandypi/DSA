# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def merge(self, a : ListNode | None, b : ListNode | None) -> ListNode | None:
        head = ListNode(0); curr = head
        while a and b:
            if a.val < b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next    
            curr = curr.next           
        if a:
            curr.next = a
        if b:
            curr.next = b
        return head.next

    def getMidNext(self, a: ListNode) -> ListNode:
        st1 = a
        st2 = a
        while st2.next and st2.next.next:
            st1 = st1.next
            st2 = st2.next.next
        next = st1.next
        st1.next = None
        return next

    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        left = head
        right = self.getMidNext(head)

        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)
                
        return self.merge(left_sorted, right_sorted)