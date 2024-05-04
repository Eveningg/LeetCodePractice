class Solution:
    def halvesAreAlike(self, string: str) -> bool:
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        firstHalf = string[0:len(string)//2]
        secondHalf = string[len(string)//2:len(string)]
        
        counterI = 0
        counterJ = 0
        for i,j in zip(firstHalf,secondHalf):
            
            if i in vowels:
                counterI += 1
                
            if j in vowels:
                counterJ += 1
        
        return True if counterI == counterJ else False