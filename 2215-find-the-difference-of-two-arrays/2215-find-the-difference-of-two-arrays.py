class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        #return answer
        #answer[0] - all ints not it nums2
        answer = [[],[]]

        nums1 = set(nums1)
        nums2 = set(nums2)
        
        for i in nums1:
            if i not in nums2:
                print(i)
                answer[0].append(i)
                
        for j in nums2:
            if j not in nums1:
                print(i)
                answer[1].append(j)

            
        return answer