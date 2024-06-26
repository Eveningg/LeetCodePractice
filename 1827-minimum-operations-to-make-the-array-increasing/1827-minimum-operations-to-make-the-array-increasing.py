class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        counter = 0
        
        for i in range(1,n):
            
            if nums[i] <= nums[i-1]:
                counter += (nums[i-1] - nums[i]) + 1
                nums[i] = nums[i-1] + 1
            
        return counter
    
