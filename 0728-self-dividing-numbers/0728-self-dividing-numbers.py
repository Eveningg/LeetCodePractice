class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
                    
        answer = []
        
        for number in range(left,right+1):
            string = str(number) 
            
            if "0" not in string: 
                divisible = True
                
                for digit in string: # 
                    
                    if number % int(digit) != 0: # 
                        divisible = False
                        break
                        
                if divisible:
                    answer.append(number) 
                    
        return answer