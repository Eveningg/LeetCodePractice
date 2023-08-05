class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        numsLength = len(nums)
        nums = set(nums)
        
        if(numsLength != len(nums)):
            return True
        
        else:
            return False