class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        counter = 0
        for i in reversed(s):
            if i.isalpha():
                counter += 1
            
            elif counter > 0:
                return counter
                
            
        return counter
                