class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #string jewels - represents types of stones that are jewels
        #stones - representing all stones you have
        
        count = 0
        
        for char in jewels:
            
            for stone in stones:
                
                if stone == char:
                    count += 1
                    
                    
        return count