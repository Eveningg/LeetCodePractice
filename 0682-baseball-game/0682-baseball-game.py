class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        score = []
        
        for i in range(len(operations)):

            if operations[i] != "C" and operations[i] != "D" and operations[i] != "+":
                score.append(int(operations[i]))
            
            elif operations[i] == "C":
                score = score[:len(score)-1]
                
            elif operations[i] == "D":
                newScore = int(score[len(score)-1]) * 2
                score.append(newScore)
                
            elif operations[i] == "+":
                a = int(score[len(score)-1])
                b = int(score[len(score)-2])
                newScore = a + b
                score.append(newScore)
            
            print(score)
        
        return sum(score)
                
        
        