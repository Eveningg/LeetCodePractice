class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        counter = 0
        
        for row in grid:
            
            for j in row:
                if j < 0:
                    counter += 1
        
        
        return counter
            