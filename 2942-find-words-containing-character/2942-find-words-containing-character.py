class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        counter = 0
        answer = []
        
        for word in words:
            if re.search(x, word):
                answer.append(counter)
                
            counter += 1
        
        return answer
                
            