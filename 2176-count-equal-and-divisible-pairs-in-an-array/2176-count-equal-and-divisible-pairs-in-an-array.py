class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        num = len(nums)
        counter = 0
        for i in range(0,num):
            
            for j in range(i+1,num):
                
                if nums[i] == nums[j] and ((i*j)%k==0):
                    counter +=1
                    
        return counter