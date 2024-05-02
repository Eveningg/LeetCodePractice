class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
         
        # returns True if:
        #   num == 0
        #   the final digit of num != 0 
        return (num == 0) or (num % 10 != 0)
            
    