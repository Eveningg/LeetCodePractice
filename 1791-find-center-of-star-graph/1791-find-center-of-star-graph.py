class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        if edges[1][0]==edges[0][0] or edges[1][0]==edges[0][1]: return edges[1][0]
        return edges[1][1]