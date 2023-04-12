class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def find_neighbors(i, j, m, n):
            neighbors = []
            if i-1 >= 0:
                neighbors.append((i-1, j))
            if j-1 >= 0:
                neighbors.append((i, j-1))
            if i+1 < m:
                neighbors.append((i+1, j))
            if j+1 < n:
                neighbors.append((i, j+1))
            return neighbors
        
        def dfs(i, j, m, n):
            grid[i][j] = "-1" # mark as visited
             
            neighbors = find_neighbors(i, j, m, n)
            
            for next_node in neighbors:
                if grid[next_node[0]][next_node[1]] == "1":
                    dfs(next_node[0], next_node[1], m, n)
            return
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j, m, n)
                    count += 1
                    
        return count
