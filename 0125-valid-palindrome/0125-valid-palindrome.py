class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Big O(n) Solution.
        
        def alphaNum(self,c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))
        
        # Solution Using In-Built Functions.
        
        newStr = ""
        
        for char in s:
            
            if char.isalnum():
                newStr += char.lower()
                
        return newStr == newStr[::-1]