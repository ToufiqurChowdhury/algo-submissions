# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Algo: two pointer with right node set to nth position ahead from left
        # move both pointer until right reach the end and left will be nth position behind
        # remove the left node and return head
        # TC: O(n)

        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n>0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next 
            right = right.next

        # remove left and set to next
        left.next = left.next.next

        return dummy.next