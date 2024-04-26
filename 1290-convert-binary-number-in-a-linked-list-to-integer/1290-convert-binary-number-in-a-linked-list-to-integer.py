# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        array = []
        
        # getting all values in node(s)
        while head:
            array.append(head.val)
            head = head.next
        
        # converting binary to decimal
        total = 0
        for digit in array:
            total = total*2 + int(digit)
        
        return total
            
