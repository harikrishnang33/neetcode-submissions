class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listHash = {}

        for s in strs:
            li = [0] * 26
            for ch in s:
                li[ord(ch) - ord('a')] += 1
            
            if tuple(li) in listHash:
                listHash[tuple(li)].append(s)
            else:
                listHash[tuple(li)] = [s]

        out = []
        for k, v in listHash.items():
            out.append(v)
        
        return out