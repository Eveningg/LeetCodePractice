class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Pointer Solution
        
        pointer = 1
        
        nums.sort()
        
        for i in nums:
            
            if pointer >= len(nums):
                return False
            
            elif i == nums[pointer]:
                return True
            
            pointer += 1
                
    
        # This solution works.
        # If the original array isn't the same size as a set of the array, then the original array had duplicate elements.
        # return len(set(nums))!=len(nums)