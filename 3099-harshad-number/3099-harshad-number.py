class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        digits = []
        tempX = x
        
        while tempX > 0:
            
            remainder = tempX % 10
            digits.append(remainder)
            tempX //= 10
            
        if x % sum(digits) == 0:
            return sum(digits)
        
        return -1
        