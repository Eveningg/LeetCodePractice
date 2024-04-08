class Solution:
    def interpret(self, command: str) -> str:
        
        newString = command.replace("()", "o")
        newString = newString.replace("(al)", "al")

        
        return newString