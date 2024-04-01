class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # n numbers of employees
        # employees numbered from 0 to n - 1
        # each employes i for hours [i]
        
        counter = 0
        pointer = 0
        
        for hour in hours:

            if hours[pointer] >= target:
                counter += 1
                pointer += 1
                
            else:
                pointer += 1
                
        
        return counter
                