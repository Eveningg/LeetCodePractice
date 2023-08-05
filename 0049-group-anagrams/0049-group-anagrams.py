class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # O(m * n) solution. n = length of strings, m equal length of array.
        # mapping character Count to list of Anagrams
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # mapping a . . . z
            
            for char in s:
                count[ord(char) - ord("a")] += 1
                
            res[tuple(count)].append(s)
            
        return res.values()
    
    
            
            
        