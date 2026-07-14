class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for ch in s:
            if ch >= 'A' and ch <= 'Z':
                string += ch.lower()
            elif ('a' <= ch <= 'z') or ('0' <= ch <= '9'):
                string += ch
        

        low = 0
        high = len(string) - 1
        while low < high:
            if string[low] == string[high]:
                low += 1
                high -= 1
            else:
                return False
        
        return True