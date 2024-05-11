class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        hash_map = {}
        
        for i in arr:
            if i not in hash_map:
                hash_map[i] = 1
                
            else:
                hash_map[i] += 1
        
        
        hash_set = []
        for value in hash_map.values():
            hash_set.append(value)
        
        return True if len(set(hash_set)) == len(hash_set) else False