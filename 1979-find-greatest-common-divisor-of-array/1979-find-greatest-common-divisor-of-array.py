class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        x,y = max(nums),min(nums)
        while y != 0:
            (x, y) = (y, x % y)
            
        return x