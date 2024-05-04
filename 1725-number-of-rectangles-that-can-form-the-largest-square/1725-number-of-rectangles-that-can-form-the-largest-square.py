class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        squares = []
        
        for i in rectangles:
            squares.append(min(i))
            
        return(squares.count(max(squares)))