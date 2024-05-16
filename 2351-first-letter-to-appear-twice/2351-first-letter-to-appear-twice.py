class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        hash_map = {}
        
        for i in range(len(s)):
            
            if s[i] not in hash_map:
                hash_map[s[i]] = 1
                
            else:
                return s[i]
            
        return -1