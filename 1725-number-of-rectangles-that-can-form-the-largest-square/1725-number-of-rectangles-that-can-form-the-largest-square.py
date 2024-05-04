class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        squares = []
        
        for i in rectangles:
            squares.append(min(i))
            
        return(squares.count(max(squares)))
    
        # Explanation:
        # The Largest Square That Can Be Made
        # Will Always Be The Smallest Dimensions (Width or Length) stored with the array rectangles.
        # Then find the largest square in the array squares, and count the amount of instances of it.