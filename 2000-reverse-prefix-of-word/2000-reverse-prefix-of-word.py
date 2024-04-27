class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        index = 0
        newStr = ""
        
        for pointer in range(len(word)):
            
            if ch == word[pointer]:
                newStr += word[pointer]
                firstSlice = word[0:pointer]
                newStr += firstSlice[::-1]
                newStr += word[pointer+1:len(word)]
                break
                
            if pointer == len(word)-1:
                return word

        
        return newStr
                