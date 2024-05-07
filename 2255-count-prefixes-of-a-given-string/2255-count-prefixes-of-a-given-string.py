class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        
        prefixArr = []
        counter = 0
        
        for pointer in range(len(s)):
            prefixArr.append(s[:pointer+1])
            
        for word in words:
            if word in prefixArr:
                counter += 1
        
        return counter