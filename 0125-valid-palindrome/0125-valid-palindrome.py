class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub ('[^a-z0-9]','',s)
        
        return s == s[::-1]
        
        
        

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        
        #1. 데이터 전처리 -> ['a','m', .. '[a]']
        s = [] 
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
                
        #2. 팰린드롬 여부 판별
        while len(strs) > 1: # 예외처리
            if strs.pop(0) != strs.pop():
                return False
            # 모두 통과했다면 True 리턴
            
    
            
                
        
