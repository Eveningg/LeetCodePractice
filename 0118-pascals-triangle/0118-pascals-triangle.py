class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        answer = [[1]]
        
        for i in range(numRows - 1):
            temp = [0] + answer[-1] + [0]
            row = []
            for j in range(len(answer[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            answer.append(row)
        return answer
        
                
                
            
            
            
        