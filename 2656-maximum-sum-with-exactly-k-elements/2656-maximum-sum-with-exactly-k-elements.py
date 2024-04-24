class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        counter = 0
        
        while k > 0:
            
            k -= 1
            counter += nums[len(nums) - 1]
            nums[len(nums) -1] = nums[len(nums) -1] + 1
            
        return counter