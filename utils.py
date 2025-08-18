class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def generate_linked_list(values):
    """
    Generate a linked list from a list of values.
    
    Args:
        values: List of values to create nodes from
        
    Returns:
        The head of the generated linked list
    """
    if not values:
        return None
        
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        
    return head


def print_linked_list(head):
    """
    Print a linked list in a readable format.
    
    Args:
        head: The head of the linked list
    """
    values = []
    current = head
    
    while current:
        values.append(str(current.val))
        current = current.next
        
    print(" -> ".join(values))

