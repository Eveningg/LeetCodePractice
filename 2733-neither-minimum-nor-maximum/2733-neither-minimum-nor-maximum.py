class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        
        counter = 0
        for num in nums:
            if num != min(nums) and num != max(nums):
                counter += 1
                ans = num
                
        return -1 if counter == 0 else ans