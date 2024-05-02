class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        counter = 0
        
        for i in range(n):
            
            if nums[i] <= nums[i-1] and i != 0:
                counter += (nums[i-1] - nums[i]) + 1
                nums[i] = nums[i-1] + 1
                
        print(nums)
        
        return counter