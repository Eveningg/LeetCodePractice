class Solution:
    def generateTheString(self, n: int) -> str:

    
        string = ""
        if n % 2 == 0:
            string = "p" * (n-1)
            string += "z"
        
        else:
            string = "h" * n
            
        return string

    