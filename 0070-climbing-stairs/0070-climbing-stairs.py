class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        hash_set = [1,1]
        
        for i in range(0,n-1):
            newNumber = hash_set[i] + hash_set[i+1]
            hash_set.append(newNumber)
                
        return newNumber
            

