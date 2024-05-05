# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # two-pointer solution
        
        slow,fast = head, head
        
        #checking if fast and next node of fast is non-null
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow