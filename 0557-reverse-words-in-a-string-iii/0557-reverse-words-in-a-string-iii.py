class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(' ')
        temp = ''
        
        for word in words:
            
            temp += word[::-1] + ' '
            
        
        return temp[0:len(temp) - 1]