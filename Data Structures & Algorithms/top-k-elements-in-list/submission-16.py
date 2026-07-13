class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1
        
        freqList = [[] for i in range(len(nums)+1)]

        for key, val in countMap.items():
            freqList[val].append(key)

        out = []
        for i in range(len(freqList)-1, 0, -1):
            for num in freqList[i]:
                out.append(num)
                if len(out) == k:
                    return out