# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head
        while curr and stack:
            last = stack.pop()
            if last == curr or curr.next == last:
                last.next = None
                break
            last.next = curr.next
            curr.next = last
            curr = curr.next.next