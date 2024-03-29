class Solution:
    # 연결된 모든 1을 큐에 넣고, visited라고 선언한 그리드가 있으면 그 안에 들어온 애들을 큐에 넣는다. (이 때 인덱스를 명시한다) 그 카운트를 세면 된다.
    # 그 다음에 순회를 돌 때 visited 그리드 안에 들어간 인덱스가 있으면 스킵, 
    def numIslands(self, grid: List[List[str]]) -> int:
        #grid와 크기가 같은 2d array initialize
        visited_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        cnt = 0
    
        # array 순회 row* column
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # row, column에 있는애가 1이고 visited에 마크가 안되어 있으면 
                if grid[i][j] == '1' and not visited_grid[i][j]:
                    self.bfs(grid,visited_grid,i,j)
                    cnt += 1
        
        return cnt
    
    def bfs(self, grid, visited_grid,i,j):
        dx = [0,1,0,-1]
        dy = [-1,0,1,0] 
        q= collections.deque()
        q.append([i,j])
        visited_grid[i][j] = 1
        
        # q에 원소가 있을 때까지 while문을 돌림
        while q:
            visited_i, visited_j = q.popleft() #visited에 들어간 애들을 꺼내서 그 다음 방향을 지정
            for k in range(4):
                next_x = visited_i + dx[k]
                next_y = visited_j + dy[k]    

                if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >=len(grid[0]) or grid[next_x][next_y] == '0' or visited_grid[next_x][next_y]:
                    continue
                q.append([next_x, next_y])
                visited_grid[next_x][next_y] = 1