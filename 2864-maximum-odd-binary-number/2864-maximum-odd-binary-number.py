class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        counter = 0
        newString = ''
        
        for char in s:
            
            if char == '1':
                counter += 1
                
        
        for i in range(len(s)-1):
            
            if counter > 1:
                newString += '1'
                counter -= 1
                
            else:
                newString += '0'
         
        # for the final bit
        if counter == 1:
            newString += '1'
            
        else:
            newString += '0'#
            
        return newString
            
            
        