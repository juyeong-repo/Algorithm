class Solution:

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        cnt = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' :
                    self.dfs(grid,i,j)
                    cnt += 1

        return cnt
            
    def dfs(self, grid, i, j) :
        if i<0 or i>= len(grid) or j<0 or j>= len(grid[0]) or grid[i][j] == '0':
            return
        
        grid[i][j] = '0'
        
        for k in range(4):
            self.dfs(grid, i+self.dx[k], j+self.dy[k])
    
    
        