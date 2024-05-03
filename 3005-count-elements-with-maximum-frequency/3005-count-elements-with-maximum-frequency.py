class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        # counting the frequency of each element in nums
        frequency = {}
        for num in nums:
            
            if num in frequency:
                frequency[num] += 1
                
            else:
                frequency[num] = 1
        
        # searching for and adding the largest frequencies together
        counter = 0
        for value in frequency.values():
            
            if value >= max(frequency.values()):
                counter += value

        return counter