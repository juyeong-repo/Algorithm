class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary initialize
        nums_map = {}
        
        # key와 value를 바꿔서 dictionary로 저장
        for i, num in enumerate(nums):
            # 원소가 key값이 된다 
            nums_map[num] = i
        
        # target에서 첫 번째 수를 뺀 결과를 key로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]
            
            
        nums_map = {}