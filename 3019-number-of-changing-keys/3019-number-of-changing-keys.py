class Solution:
    def countKeyChanges(self, s: str) -> int:
        
        lastLetter = s[0].lower()
        total = 0
        
        for pointer in range(1,len(s)):
            
            if s[pointer].lower() != lastLetter:
                total += 1
            
            lastLetter = s[pointer].lower()
            
        
        
        return total