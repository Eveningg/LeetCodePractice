class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        evenNumbers = 0
        for num in nums:
            counter = 0
            while num != 0:
                num = num // 10
                counter += 1
                
            if counter % 2 == 0:
                evenNumbers += 1
        
        return evenNumbers