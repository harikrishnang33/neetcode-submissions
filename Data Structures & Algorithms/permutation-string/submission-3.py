class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Hash = {}
        for ch in s1:
            s1Hash[ch] = 1 + s1Hash.get(ch, 0)
        
        left = 0
        right = left
        checkHash = {}
        while right < len(s2):
            checkHash[s2[right]] = 1 + checkHash.get(s2[right], 0)
            right += 1
            if right - left == len(s1):
                if s1Hash == checkHash:
                    return True
                else:
                    checkHash = {}
                    left += 1
                    right = left

        
        return False