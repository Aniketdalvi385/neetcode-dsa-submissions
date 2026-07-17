# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Brute force approach with stack
        # stack = []
        # curr = head
        # while curr:
        #     stack.append(curr)
        #     curr = curr.next

        # curr = head
        # while curr and stack:
        #     last = stack.pop()
        #     if last == curr or curr.next == last:
        #         last.next = None
        #         break
        #     last.next = curr.next
        #     curr.next = last
        #     curr = curr.next.next

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None        
        curr, prev = second, None
        while curr:
            n_node = curr.next
            curr.next = prev
            prev = curr
            curr = n_node

        list1, list2 = head, prev

        while list2:
            list1_next = list1.next
            list2_next = list2.next
            list1.next = list2
            list2.next = list1_next
            list1 = list1_next
            list2 = list2_next

        
