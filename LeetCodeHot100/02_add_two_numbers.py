from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode()
        new_node_0 = new_node
        next_val = 0
        while l1 and l2:
            next_val, new_val = divmod(l1.val + l2.val + next_val, 10)
            new_node.next = ListNode(new_val)
            new_node = new_node.next 
            l1 = l1.next
            l2 = l2.next
        while l1:
            next_val, new_val = divmod(l1.val + next_val, 10)
            new_node.next = ListNode(new_val)
            new_node = new_node.next 
            l1 = l1.next
        while l2:
            next_val, new_val = divmod(l2.val + next_val, 10)
            new_node.next = ListNode(new_val)
            new_node = new_node.next 
            l2 = l2.next
        if next_val:
            new_node.next = ListNode(next_val)
        new_node_0 = new_node_0.next
        return new_node_0