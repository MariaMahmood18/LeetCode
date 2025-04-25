# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # Strategy no.1

        # Create two pointers p and q, pointing at head node.
        p = head # moves 2 nodes at a time
        q = head # moves 1 node at a time

        # Traverse the list until q reaches end
        # Keep going while there are at least 2 nodes ahead.
        # This prevents errors when q tries to jump two steps (q = q.next.next).
        while q and q.next:
            p = p.next
            q = q.next.next
        return p


        # # Strategy no.2

        # # First pass: Get the length of linked list
        # count = 0
        # current = head
        # while current:
        #     count += 1
        #     current = current.next

        # # Second pass: Go to second middle node
        # mid = count // 2
        # current = head
        # for _ in range(mid):
        #     current = current.next

        # return current

        


        