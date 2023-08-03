class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closeToOpen = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        # Checking if character is equal to a closing bracket
        # Then check if the value of the stack before the current character is a corresponding open bracket
        # We then remove these elements from our stack, as we know they're valid.
        for char in s:
            
            if char in closeToOpen:
                
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                    
                else:
                    return False
            
            # Appending the character to our stack, as it is a open bracket
            else:
                stack.append(char)
                
        # Returning true if our stack is empty, meaning all open brackets had corresponding closing brackets
        
        return True if not stack else False
                