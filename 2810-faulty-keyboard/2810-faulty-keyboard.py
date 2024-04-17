class Solution:
    def finalString(self, s: str) -> str:
        
        answer = ''
        
        for pointer in range(len(s)):
            
            if s[pointer] == 'i':
                answer = answer[::-1]
                
            else:
                answer += s[pointer]
        
        return answer