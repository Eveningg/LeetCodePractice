class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        ans = []
        hash_map = {}
        
        # Finding the repeated number
        for i in grid:
            for j in i:
                if j not in hash_map:
                    hash_map[j] = 1
                    
                else:
                    ans.append(j) 
        
        if 1 not in hash_map.keys():
            ans.append(1)
            return ans
        
        # Finding the missing numbers
        for num in range(min(hash_map.keys()), max(hash_map.keys())+1):
            if num not in hash_map.keys():
                ans.append(num)
                return ans
            
        # if no missing number, the missing number is +1 of max hash_map.keys()
        ans.append(max(hash_map.keys()) + 1)
        return ans