class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        maxLen = 0
        seenChar = set()

        for high in range(len(s)):
            while s[high] in seenChar:
                seenChar.remove(s[low])
                low += 1
            
            seenChar.add(s[high])
            maxLen = max(maxLen, high - low + 1)
        
        return maxLen