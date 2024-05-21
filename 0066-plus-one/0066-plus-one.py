class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        string = ""
        hashSet = []
        
        for num in digits:
            string += str(num)
            
        string = int(string) + 1
        
        while string > 0:
            remainder = string % 10
            hashSet.append(remainder)
            string //= 10
            
        return reversed(hashSet)