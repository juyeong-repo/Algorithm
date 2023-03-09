import numpy as np

def solution_numpy(board):
    '''
    예외처리를 어떻게 해줘야할지 모르겠다!
    1. 넘파이 사용
    2차원 배열은 넘파이를 사용하면 쉽게 풀수있다.
   
    '''

board = np.array(board)

# print (np.where(board == 1)) 
# (array([2,3]), array([2,2]))

rows, cols = np.where(board == 1)
for r , c in zip (rows, cols):
    board[r-1: r+2, c-1: c+2] = 1

print (board)
#  이 때 0인 것을 count 하면 된다 -> 이 때 행렬 범위를 넘어간다면??






solution_numpy([[0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 1, 0, 0], 
                [0, 0, 1, 0, 0], 
                [0, 0, 0, 0, 0]]
)



    