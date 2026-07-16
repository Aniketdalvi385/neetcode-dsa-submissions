# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pt1 = list1
        pt2 = list2
        head = None
        if pt1 is None:
            return list2
        elif pt2 is None:
            return list1

        if pt1 and pt2 and pt1.val < pt2.val:
            head = pt1
            pt1 = pt1.next
        else:
            head = pt2
            pt2 = pt2.next
        
        curr = head
        
        while pt1 and pt2:
            if pt1.val < pt2.val:
                curr.next = pt1
                pt1 = pt1.next
                curr = curr.next
            else:
                curr.next = pt2
                pt2 = pt2.next
                curr = curr.next
        print(curr.val)
        if pt1:
            curr.next = pt1
        elif pt2:
            curr.next = pt2
        return head