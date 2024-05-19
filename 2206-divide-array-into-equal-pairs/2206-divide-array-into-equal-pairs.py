class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        

        for i in Counter(nums):
            if Counter(nums)[i]%2==1:
                return False
        return True
        