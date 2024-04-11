class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
    
        target = []
        
        # using insert - but not the package
        
        for n,i in zip(nums,index): 
            target[i:i] = [n]
        return target
    
        # using insert solution
        
        for num in range (len(nums)):
            
            indexNum = index[num]
            target.insert(indexNum, nums[num])
            
        return target
        
        
        