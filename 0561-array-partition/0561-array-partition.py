class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        

        nums.sort()
        total = 0
        start,end,step = 0,len(nums),2
        
        for i in range(start,end,step):
            total += nums[i]
            
        return total
        
        # explaination:
        # if you sort the list into pairs of two numbers
        # the smallest value of the pair will always be the left-most digit
        # therefore, you can iterate through the list equal to the pair size you would make
        # taking the left-most value
        