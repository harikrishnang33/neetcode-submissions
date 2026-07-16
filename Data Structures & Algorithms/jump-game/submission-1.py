class Solution:
    def canJump(self, nums: List[int]) -> bool:
        near = 0
        far = 0
        
        while far < len(nums) - 1:
            farthest = 0
            for i in range(near, far+1):
                farthest = max(farthest, i + nums[i])
            
            near = far + 1
            far = farthest
            if near > far:
                return False
        return True