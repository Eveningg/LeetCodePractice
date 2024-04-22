class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # O(nlogn) complexity
        nums.sort()
        num1 = nums[len(nums)-1] - 1
        num2 = nums[len(nums)-2] - 1
        
        return num1*num2
    
        # O(n) complexity
        
        first, second = 0, 0
        
        for number in nums:
            
            if number > first:
                # update first largest and second largest
                first, second = number, first
                
            elif number > second:
                # update second largest
                second = number
        
        return (first - 1) * (second - 1)