class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        if not self.root:
            self.root = ListNode(value)

        else:
            curr = self.root
            while curr.next:
                curr = curr.next
            curr.next = ListNode(value)
        self.size += 1

    def print_list(self):
        curr = self.root
        while curr:
            print(curr.val)
            curr = curr.next

    def bubble_sort(self):
        curr = self.root
        swapping = True
        i = 0

        while swapping:
            swapping = False
            prev = None
            while curr.next:
                if curr.next.val < curr.val:
                    if not prev:
                        self.root = curr.next
                        curr = curr.next
                        prev = True
                    else:
                        temp = curr.next
                        curr.next = curr.next.next
                        curr = temp
                    if not curr.next:
                        curr = self.root
                    swapping = True


LL = LinkedList()

LL.insert(6)
LL.insert(4)
LL.insert(8)
LL.insert(1)
LL.bubble_sort()
LL.print_list()
print(LL.size)
