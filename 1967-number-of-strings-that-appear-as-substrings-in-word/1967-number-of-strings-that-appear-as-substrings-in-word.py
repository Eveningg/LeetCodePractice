class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        # O(N) solution
        
        count=0
        
        for i in patterns:
            if i in word:
                count += 1
                
        return count
        
        
        
        substrings = []
        total = 0

        # brute-force solution
        for i in range(len(word)):

            for j in range(i+1,len(word)+1):
                substrings.append(word[i:j])

        for pattern in patterns:
            if pattern in substrings:
                total += 1

        return total