class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # hidden integer arr consiting of n integers
        # encoded 
        
        arr = [first]
        
        # iterating through encoded, '^' means XOR
        for i in range(len(encoded)):
            arr.append(arr[i] ^ encoded[i])
            
        return arr