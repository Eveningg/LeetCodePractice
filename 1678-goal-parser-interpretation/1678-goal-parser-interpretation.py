class Solution:
    def interpret(self, command: str) -> str:
        
        newString = command.replace("()", "o").replace("(al)", "al")

        
        return newString