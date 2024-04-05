class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        ans = 0
        
        for i in range(len(nums)):  # nums = [0,1,4,6,7,10],  diff = 3
            j = nums[i] - diff  # 4 - 3 = 1 (when i ==2)
            k = diff + nums[i]  # 3 + 4 = 7 (when i ==2)
            if j in nums and k in nums: # 1 and 7 is there in the list
                ans +=1
        return ans