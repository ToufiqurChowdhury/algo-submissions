# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #1 2 4
        #    ^
        #1 3 4 5
        #      ^

        # 1 1 2 3 4 4 5
        #            ^
        #^(dummy)

        # tail and dummy pointer

        dummy = ListNode()
        tail = dummy

        #List traverse loop
        while list1 and list2:

            # check for list1 node val <= list2 node val
            if list1.val <= list2.val:
                # add lower value node to tail and move list1 pointer forward
                tail.next = list1
                list1 = list1.next
            else:
                # add lower value node to tail and move list2 pointer forward
                tail.next = list2
                list2 = list2.next

            # move tail node forward            
            tail = tail.next

         # add remaining nodes to the tail
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        #return starting node
        return dummy.next
        