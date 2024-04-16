class Solution:
    def scoreOfString(self, s: str) -> int:
        
        counter = 0
        
        for pointer in range(len(s)):
            
            if pointer > 0:
                counter += abs(ord(s[pointer]) - ord(s[pointer-1]))
        
        return counter