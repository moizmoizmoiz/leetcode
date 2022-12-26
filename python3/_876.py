# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 2 pointers

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(-1, head)

        fast = newHead
        slow = newHead

        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
            slow = slow.next
        return slow

