class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        sequenceLen = 0

        for num in numSet:
            if (num-1) not in numSet:
                seqLen = 1
                while (num+seqLen) in numSet:
                    seqLen += 1
                if seqLen > sequenceLen:
                    sequenceLen = seqLen

        return sequenceLen