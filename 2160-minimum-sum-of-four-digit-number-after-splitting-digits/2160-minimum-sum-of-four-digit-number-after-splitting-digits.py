class Solution:
    def minimumSum(self, num: int) -> int:
        
        #sorting the four digits in num
        # means that 1 and 3, 2 and 4th position integers
        # will always be teh smallest sums
        
        digits = []

        for i in str(num):
            digits.append(i)

        digits.sort()

        return int(digits[0] + digits[2]) + int(digits[1] + digits[3])
        