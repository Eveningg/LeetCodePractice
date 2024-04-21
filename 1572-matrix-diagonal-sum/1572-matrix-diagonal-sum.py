class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
        counter = 0
        matrixRowLength = len(mat) - 1
        
        for pointer in range(len(mat)):
            
            #checking if the columns + rows are equal
            if matrixRowLength - pointer == pointer:
                counter += mat[pointer][pointer]
                
            else:
                counter += mat[pointer][pointer]
                counter += mat[pointer][matrixRowLength - pointer]
            
        return counter