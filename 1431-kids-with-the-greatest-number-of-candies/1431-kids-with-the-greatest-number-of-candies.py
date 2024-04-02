class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #n kids with candies
        #integer candies, where candies[i] represents number of candies
        #integer extraCandies denoting number of extracandies i have
        
        pointer = 0
        answer = []
        
        for i in candies:
            
            if candies[pointer] + extraCandies >= max(candies):
                answer.append(True)
                
            else:
                answer.append(False)
                
            pointer += 1
                
        return answer