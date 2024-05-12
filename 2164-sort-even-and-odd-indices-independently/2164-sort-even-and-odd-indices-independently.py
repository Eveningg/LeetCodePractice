class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        oddIndicies = []
        evenIndicies = []
        for i in range(1,len(nums)+1):
            if i % 2 == 1:
                oddIndicies.append(nums[i-1])
            
            else:
                evenIndicies.append(nums[i-1])
                
        oddIndicies.sort()
        evenIndicies.sort(reverse=True) 
        n = len(oddIndicies) + len(evenIndicies)
        counter = 0
        answer = []
        for i in range(1,n+1):
            
            if i % 2 == 1:
                answer.append(oddIndicies[counter])
            
            else:
                answer.append(evenIndicies[counter])
                counter +=1

        return answer