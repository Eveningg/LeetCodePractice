class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        counter = 0
        
        matrixRowLength = len(mat) - 1
        
        for pointer in range(len(mat)):
            
            if matrixRowLength - pointer == pointer:
                counter += mat[pointer][pointer]
                
            else:
                counter += mat[pointer][pointer]
                counter += mat[pointer][matrixRowLength - pointer]
            
        return counter