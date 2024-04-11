class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
    
        target = []
        
        for num in range (len(nums)):
            
            indexNum = index[num]
            target.insert(indexNum, nums[num])
            
        return target
        