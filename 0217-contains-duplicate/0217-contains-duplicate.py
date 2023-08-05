class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Using Hashset
                
        hashset = set()
        
        for num in nums:
            
            # if number checked in hashset, return true because duplicates exist.
            if num in hashset:
                return True
            
            hashset.add(num)
            
        return False
        
    
        # This solution works.
        # If the original array isn't the same size as a set of the array
        # Then the original array had duplicate elements. 
        # Just thought it was a funny solution.
        
        # return len(set(nums))!=len(nums)