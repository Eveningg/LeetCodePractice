class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        for num in range(0,len(nums)):
            ans.append(nums[nums[num]])
        
        return(ans)
    
        