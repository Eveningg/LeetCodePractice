class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        
        counter = 0
        maximum,minimum = max(nums),min(nums)

        for num in nums:
            if num != minimum and num != maximum:
                counter += 1
                ans = num
                
        return -1 if counter == 0 else ans