class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        empty = ''
        empty2 = ''
        
        for char in word1:
            
            empty += char
            
        for char in word2:
            
            empty2 += char
            
        if empty == empty2:
            return True
        
        return False
            