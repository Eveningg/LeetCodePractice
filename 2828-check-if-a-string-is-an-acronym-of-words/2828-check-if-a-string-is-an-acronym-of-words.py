class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        
        empty = ''
        
        for word in words:
            
            empty += word[0]
            
        
        if s == empty:
            return True
        
        return False