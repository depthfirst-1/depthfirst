# Iterative
def reverse_list_1(head):
    curr = head
    prev = None

    while curr:
        curr = curr.next
        head.next = prev
        prev = head
        head = curr
    return prev


# Recursive
def reverse(node):
    # If the caller passes in an empty linked list,
    # or if we have reached the end of the linked list. 
    if node is None or node.next is None:
        return node

    reversed_list_head = reverse(node.next)
    # Get the last node after the list is reversed. 
    last_node = node.next
    # Set the current node as last_node's next element.
    last_node.next = node
    node.next = None
    
    return reversed_list_head
