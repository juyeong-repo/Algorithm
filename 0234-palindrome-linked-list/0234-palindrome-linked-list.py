# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q : deque = collections.deque()
        
        # base case : node는 1~10의 5승까지라 isalnum()으로 체크해줄 필요x
        
        if not head:
            return True
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next 
        
        # linkedlist를 돌면서 (linkedNode는 len이 없다)
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
            
            
        return True
            
        