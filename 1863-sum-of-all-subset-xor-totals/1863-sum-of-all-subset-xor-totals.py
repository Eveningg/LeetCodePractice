class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        ans = 0
        for mask in range(1 << len(nums)): 
            val = 0
            for i in range(len(nums)): 
                if mask & 1 << i: val ^= nums[i]
            ans += val
        return ans 
                
        
        
        