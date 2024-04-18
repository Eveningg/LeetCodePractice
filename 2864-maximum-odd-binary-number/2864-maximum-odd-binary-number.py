class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        counter = 0
        newString = ''
        
        # counting the amount of '1's
        for char in s:
            
            if char == '1':
                counter += 1
                
        
        # creating a new string, 1's go first, then 0's
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
            newString += '0'
            
        return newString
            
            
        