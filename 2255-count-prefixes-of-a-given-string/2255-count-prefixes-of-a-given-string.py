class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        
        counter=0
        
        for word in words:
            if (s[:len(word)]==word):
                counter += 1
                
        return counter