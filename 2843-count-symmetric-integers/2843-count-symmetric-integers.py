class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        counter = 0 
        for i in range(low,high+1):
            if len(str(i)) % 2 == 0:
                
                hash_set = [int(d) for d in str(i)]
                firstHalf = hash_set[:len(hash_set) // 2]
                secondHalf = hash_set[len(hash_set) // 2:]
                
                if sum(firstHalf) == sum(secondHalf):
                    counter += 1
                
        return counter
        