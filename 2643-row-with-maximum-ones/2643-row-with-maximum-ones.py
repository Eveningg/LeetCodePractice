class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        oneCounter = 0
        for i in range(len(mat)):
            if mat[i].count(1) > oneCounter:
                oneCounter = mat[i].count(1)
                index = i
            
        return [0,0] if oneCounter == 0 else [index,oneCounter]