# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Brute force Time Complexity: O(n) Space Complexity: O(1)
        # prev = None
        # curr = head

        # while curr:
        #     n_node = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = n_node

        # return prev

        #Dynamic programming Solution
        if head is None or head.next is None:
            return head

        f = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return f