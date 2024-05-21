class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        binarySum = int(a,2) + int(b,2)
        string = bin(binarySum)
        return string[2:]