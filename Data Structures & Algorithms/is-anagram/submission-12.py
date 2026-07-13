class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sHash, tHash = {}, {}

        for ch in s:
            sHash[ch] = sHash.get(ch, 0) + 1
        for ch in t:
            tHash[ch] = tHash.get(ch, 0) + 1

        return sHash == tHash