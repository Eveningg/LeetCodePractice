class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        
        counter = 0
        pointer = 0
        
        for hour in hours:

            if hours[pointer] >= target:
                counter += 1
            
            pointer += 1
                
        
        return counter
                