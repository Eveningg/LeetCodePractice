class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        return len(list(set(nums) - {0}))
    
        counter = 0
        # Checking Array Has Numbers Greater Than 0
        while max(nums) != 0:
            counter += 1
            smallestNonZero = min(i for i in nums if i > 0)
            for pointer in range(len(nums)):
                if nums[pointer] != 0:
                    nums[pointer] -= smallestNonZero
                    if nums[pointer] < 0:
                        nums[pointer] = 0
                
                
             
        
        return counter
                
                

            
 