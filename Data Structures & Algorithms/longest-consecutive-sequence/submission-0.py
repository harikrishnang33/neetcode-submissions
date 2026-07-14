class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        sequenceLen = 0

        for num in numSet:
            seqLen = 1
            number = num
            while number+1 in numSet:
                seqLen += 1
                number += 1
            if seqLen > sequenceLen:
                sequenceLen = seqLen

        return sequenceLen