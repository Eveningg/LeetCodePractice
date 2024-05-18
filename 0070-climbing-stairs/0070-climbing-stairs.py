class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        hash_set = [1,1]
        
        for i in range(n-1):
            newNumber = hash_set[i] + hash_set[i+1]
            hash_set.append(newNumber)
            print(hash_set)
                
        return newNumber
            

