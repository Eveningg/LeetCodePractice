class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        
        n = len(nums)
        total = 0

        for counter in range(len(nums)):

            if n % (counter+1) == 0:
                total += nums[counter] * nums[counter]
                                             
        return total