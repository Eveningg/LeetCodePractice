class Solution:
    def romanToInt(self, s: str) -> int:
        
        # Assigning values for each roman numeral, using a dictionary
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        number = 0
        
        #Replacing All Possible Alternative Cases With Simpler Form
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        
        #Iterating Through Characters In String, assigning character value to variable 'number'
        for char in s:
            number += values[char]
            
        return number
            