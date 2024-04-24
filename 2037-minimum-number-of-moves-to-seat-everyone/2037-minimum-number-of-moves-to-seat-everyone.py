class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        counter = 0
        
        #O(NlogN) + O(NlogN)
        seats.sort()
        students.sort()
        
        #O(N)
        for pointer in range(len(students)):
            
            counter += abs(students[pointer] - seats[pointer])
            
        return counter
            
            
            
            
        