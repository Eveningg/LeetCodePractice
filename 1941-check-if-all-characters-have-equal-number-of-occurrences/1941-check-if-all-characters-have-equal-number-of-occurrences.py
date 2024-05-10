class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        hash_map = {}
        
        for char in s:
            
            if char not in hash_map:
                hash_map[str(char)] = 1
            
            else:
                hash_map[str(char)] += 1
        
        compare = hash_map.get(str(s[0:1]))
        for value in hash_map.values():
            if compare != value:
                return False
        
        return True
    
