class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hash_map = {}
        
        for i in range(len(s)):
            
            if s[i] not in hash_map:
                hash_map[str(s[i])] = 1
                
            else:
                hash_map[s[i]] += 1
        
        for char, value in hash_map.items():
            
            if value == 1:
                return s.find(char)
                
        
        return -1