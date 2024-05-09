class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums.append(max(nums))
        nums.append(min(nums))
        nums = nums[n:]
        
        x,y = nums[0],nums[1]
        while y != 0:
            (x, y) = (y, x % y)
            
        return x