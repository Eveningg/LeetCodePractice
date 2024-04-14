class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        elementSum = 0
        digitSum = []
        
        for num in nums:
            elementSum += num
            
            if num > 9:
                 
                # converting two or greater numbers into digits, then appending to digitSum
                while num > 0:
                    
                    remainder = num % 10
                    digitSum.append(remainder)
                    num //= 10
                    
            else:
                digitSum.append(num)
                
                
        return(elementSum - sum(digitSum))
            
        