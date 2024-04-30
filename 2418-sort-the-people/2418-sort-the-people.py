class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        hash = dict(zip(heights,names))
        
        names.clear()
        heights.sort(reverse=True)
        for height in heights:
            names.append(hash[height])
            
        return names
        