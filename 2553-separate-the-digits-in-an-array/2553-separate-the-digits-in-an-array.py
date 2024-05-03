class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        answer = []
        
        for num in nums:
            digit_list = list(map(int, str(num)))
            answer.extend(digit_list)
            
        return answer