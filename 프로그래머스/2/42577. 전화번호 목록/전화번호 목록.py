def solution(phone_book):
    phone_book.sort() #O(NlogN)
    
    for i in range(len(phone_book) -1):
        # 인접한 번호 비교
        current = phone_book[i]
        next_value = phone_book[i+1]
        if next_value.startswith(current):
            return False
    return True

