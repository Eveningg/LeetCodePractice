class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        nums.sort()
        arrLength = len(nums) - 1

        return nums[arrLength] * nums[arrLength-1] - nums[0] * nums[1]