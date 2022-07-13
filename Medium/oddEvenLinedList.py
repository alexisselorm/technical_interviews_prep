class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        odd = head
        even = odd.next
        even_head = even
        while even != None and even.next != None:
            odd.next = even.next  # Connecting 1 to 3
            odd = odd.next  # pointer now at 3
            even.next = odd.next  # Connecting 2 to 4
            even = even.next  # Pointer for even now at 4
        odd.next = even_head  # Linking the last odd index with the first even index
        return head
