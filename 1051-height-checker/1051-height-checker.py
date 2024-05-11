class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)
        counter = 0
        for pointer in range(len(heights)):
            if heights[pointer] != expected[pointer]:
                counter += 1
            
        return counter