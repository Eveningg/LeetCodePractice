class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        nums.sort()
        num1 = nums[len(nums)-1] - 1
        num2 = nums[len(nums)-2] - 1
        
        return num1*num2