class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        squares = []
        
        for dimensions in rectangles:
            
            squares.append(min(dimensions))
            
        return(squares.count(max(squares)))