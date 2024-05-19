class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        # return [numOfPairs, amountLeft]
        
        numsOfPairs = 0
        hashSet = []
        
        for i in range(len(nums)):
            
            if nums[i] not in hashSet:
                hashSet.append(nums[i])
                
            else:
                numsOfPairs += 1
                hashSet.remove(nums[i])
        
        return[numsOfPairs,len(hashSet)]