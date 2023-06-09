class Solution:
    def isValid(self, s: str) -> bool:
        # 스택을 사용한다.
        # stack 을 직접 구현해야 하는가? x 파이썬의 리스트는 push,pop모두 O(1) 에 동작한다.
        
        stack = []
        
        # 딕셔너리 형으로 선언 
        table = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        
        
        # 테스트 케이스를 고려하여 예외처리가 필요하다.
        for char in s:
            if char not in table: 
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
            
        return len(stack) == 0
        