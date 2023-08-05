class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for counter, num in enumerate(nums):
        
            for counter2, num2 in enumerate(nums):
            
                if(num + num2 == target and counter != counter2):
                
                    return counter, counter2
            

    