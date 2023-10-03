class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, key) -> None:
        # create head if it does not already exist
        if not self.head:
            self.head = ListNode(key)
            return

        curr = self.head
        # Enumerate to the last node of the list
        while curr.next:
            curr = curr.next
        curr.next = ListNode(key)

    def length(self) -> int:
        curr = self.head
        count = 0

        while curr:
            count += 1
            curr = curr.next

        return count

    def search(self, key) -> ListNode:
        curr = self.head
        while curr and curr.value != key:
            curr = curr.next
        return curr
