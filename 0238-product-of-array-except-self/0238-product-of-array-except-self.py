class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        out = []
        num = 1
        
        # 왼쪽 
        num = 1
        for i in range(len(nums)):
            out.append(num)
            num *= nums[i]
        
        
        # 오른쪽 (nums 배열의 끝에서부터 거꾸로 for 문 돌며 곱하기)
        num = 1
        for i in range(len(nums)-1,-1,-1):
            out[i] *= num
            num *= nums[i]
        
        return out