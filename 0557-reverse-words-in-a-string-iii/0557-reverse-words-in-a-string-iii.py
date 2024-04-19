class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(' ')
        temp = ''
        
        for pointer in range(len(words)):
            
            word = words[pointer]
            temp += word[::-1] + ' '
        
        return temp[0:len(temp) - 1]