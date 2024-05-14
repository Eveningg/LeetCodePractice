class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        
        hash_set = []
        n = len(mountain) - 1
 
        for i in range(1,n):
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                hash_set.append(i)
        
        return hash_set