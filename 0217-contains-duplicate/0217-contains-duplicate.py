class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        print(nums)
        print(set(nums))
        
        numsLength = len(nums)
        
        nums = set(nums)
        
        if(len(nums) != numsLength):
            return True