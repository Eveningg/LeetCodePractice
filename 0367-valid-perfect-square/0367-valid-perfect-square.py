class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if int(num**0.5)*int(num**0.5)==num:
	        return True
        else:
	        return False