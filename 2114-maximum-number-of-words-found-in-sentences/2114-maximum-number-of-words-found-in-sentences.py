class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        m=0
        
        for i in sentences:
            m=max(m,i.count(" ")+1)
            
        return m

        # big O(N^2 + N) Algorithm - Not Best.
        
        counter = 1
        empty = []
        
        for sentence in sentences:
            
            for char in sentence:
                if char == " ":
                    counter += 1
            
            empty.append(counter)
            counter = 1
        
        return(max(empty))
    
    