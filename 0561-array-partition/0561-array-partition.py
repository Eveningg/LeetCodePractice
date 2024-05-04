class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        sum_ = 0
        for i in range(0,len(nums),2):
            sum_ += nums[i]
        return sum_
    
        nums.sort()
        pairs = []
        start,n,step = 0,len(nums),2
        
        for i in range(0,n,step):
        
            pairs.append(nums[i:i+step])
        
        counter = 0
        for pair in pairs:
            
            counter += min(pair)
        
        return counter
                
        