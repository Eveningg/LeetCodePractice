class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        counter = 0
        
        seats.sort()
        students.sort()
        
        # we KNOW they are same length.
        
        for pointer in range(len(students)):
            
            counter += abs(students[pointer] - seats[pointer])
            
        return counter
            
            
            
            
        