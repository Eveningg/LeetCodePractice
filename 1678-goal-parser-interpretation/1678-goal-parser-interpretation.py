class Solution:
    def interpret(self, command: str) -> str:
        #command that consistents of strings: "G", "()", "(al)"
        
        newString = command.replace("()", "o")
        newString = newString.replace("(al)", "al")

        
        return newString