class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = [0]
        
        for i in range(1,n+1):
            binary = bin(i)
            numOfOnes = binary[2:].count("1")
            ans.append(numOfOnes)
            
        return ans
            
        