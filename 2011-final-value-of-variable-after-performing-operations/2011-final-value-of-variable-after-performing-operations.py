class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        X = 0
        
        for chars in operations:
            
            if chars == "--X" or chars == "X--":
                X -= 1
                
            elif chars == "++X" or chars == "X++":
                X += 1
                
        return X
        