class ListNode:
    next = None
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return str(self.val) + "-->" + str(self.next)

class MyLinkedList:
    head = None
    count = 0

    def __init__(self):
        self.head = ListNode(None)

    def get(self, index: int) -> int:
        if index >= self.count:
            return -1

        cur = self.head
        for i in range(index+1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        nnode = ListNode(val)

        # head -> nnode -> rest
        nnode.next = self.head.next
        self.head.next = nnode

        self.count += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next:
            cur = cur.next
        nnode = ListNode(val)
        cur.next = nnode

        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:    
        if index > self.count:
            return -1

        cur = self.head
        for i in range(index):
            if cur.next:
                cur = cur.next
        rest = cur.next
        nnode = ListNode(val)

        # cur nnode rest
        cur.next = nnode
        nnode.next = rest

        self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.count:
            return -1

        prev = self.head
        for i in range(index):
            prev = prev.next
        if not prev:
            return None
        cur = prev.next
        if cur:
            rest = cur.next
        else:
            rest = None
        del cur
        prev.next = rest

        self.count -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)