class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        
        n = len(nums)
        total = 0

        for counter in range(1, len(nums)+1):

            if n % counter == 0:
                total += nums[counter-1] * nums[counter-1]
                                             
        return total