
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue
            target = -num
            if target < 0:
                break
            low = index + 1
            high = len(nums) - 1
            while low < high:
                lowNum = nums[low]
                highNum = nums[high]
                res = lowNum + highNum
                if res < target:
                    low += 1
                    while nums[low] == lowNum and low < high:
                        low += 1
                elif res > target:
                    high -= 1
                    while nums[high] == highNum and low < high:
                        high -= 1
                else:
                    triplets.append([num, nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while nums[low] == lowNum and low < high:
                        low += 1
                    while nums[high] == highNum and low < high:
                        high -= 1
            
        return triplets
