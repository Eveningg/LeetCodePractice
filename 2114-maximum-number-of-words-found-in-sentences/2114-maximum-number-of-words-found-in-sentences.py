class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        # big O(N^2) Algorithm - Not Best.
        
        counter = 1
        empty = []
        
        for sentence in sentences:
            
            for char in sentence:
                if char == " ":
                    counter += 1
            
            empty.append(counter)
            counter = 1
        
        return(max(empty))