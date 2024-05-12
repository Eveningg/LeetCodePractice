class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        hash_set = []
        
        for num in nums:
            if num % 2 == 1:
                hash_set.append(num)
                
            else:
                hash_set.insert(0,num)
                
        return hash_set