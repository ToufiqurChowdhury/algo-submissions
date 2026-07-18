# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # set slow and fast pointer to head
        slow, fast = head, head

        # loop until fast reach the end
        while fast and fast.next:
            # fast moves twice faster than slow
            slow = slow.next
            fast = fast.next.next

            # when fast meets slow, cycle is found and return true
            if slow == fast:
                return True

        # fast reached end of the list and reaturn false
        return False