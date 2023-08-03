# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Overall algorithm compares each element in nodes sequentially, placing smallest value in dummyNode
        
        # dummyNode = temp node to act as temp storage
        # Tail - equals the value of dummyNode
        dummyNode = ListNode()
        tail = dummyNode
        
        # While loops iterates until one list is empty
        while list1 and list2:
            
            # Placing the smallest value of both lists into dummyNode, then moving to next element of corresponding node
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            
            else:
                tail.next = list2
                list2 = list2.next
            
            #moving onto next node position after executing above conditionals
            tail = tail.next
        
        # Add either list1 or list2 to the end of our dummyNode, as the lists are already sorted
        if list1:
            tail.next = list1
            
        elif list2:
            tail.next = list2
            
        return dummyNode.next
        
                
        
        