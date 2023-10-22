class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums) :
            compliment = target - n

            if compliment in nums[i+1:]:
                return [nums.index(n),nums[i+1:].index(compliment) + (i+1)]