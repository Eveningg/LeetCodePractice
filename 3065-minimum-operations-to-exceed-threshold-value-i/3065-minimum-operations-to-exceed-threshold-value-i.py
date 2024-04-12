class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        #int arr nums
        #int k
        
        counter = 0
        
        for num in nums:
            
            if k > num:
                counter += 1
                
        return counter
            