class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        priorityQueue = []
        countMap = {}

        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1

        for key, val in countMap.items():
            heapq.heappush(priorityQueue, (-val, key))

        out = []
        for i in range(k):
            out.append(heapq.heappop(priorityQueue)[1])

        return out