class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, j in enumerate(nums):

            for o, p in enumerate(nums):

                if p + j == target and i != o:
                    return(i, o)

    