class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        answer = []
        
        for counter in range(len(nums)):
            
            if counter % 2 == 1 or counter == 1:
                
                freq = nums[counter - 1]
                value = nums[counter]
                
                answer += [value] * freq
                
        return answer