class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        score = []
        
        for i in range(len(operations)):

            if operations[i] == "C":
                score.pop()
                
            elif operations[i] == "D":
                newScore = int(score[len(score)-1]) * 2
                score.append(newScore)
                
            elif operations[i] == "+":
                newScore = int(score[len(score)-1]) + int(score[len(score)-2])
                score.append(newScore)
            
            else:
                score.append(int(operations[i]))
        
        return sum(score)
                
        
        