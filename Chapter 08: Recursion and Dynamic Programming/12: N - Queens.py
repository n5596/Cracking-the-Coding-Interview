class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        all_grids = []
        
        def add_grid(rows):
            glist = [["." for j in range(n)] for i in range(n)]
            for r in rows.keys():
                glist[r][rows[r]] = "Q"
                
            grid = []
            for g in glist:
                grid.append("".join(g))
                
            all_grids.append(grid)
            return
        
        def check_possible_arrangement(rows, r1, c1):
            for r2 in rows.keys():
                c2 = rows[r2]
                
                if abs(r1-r2) == abs(c1-c2):
                    return False
            return True
                
        def recurse(r, n, rows):
            if r == n: # found a valid arrangement
                add_grid(rows)
                return
            
            cols_used = set(rows.values())
            cols_possible = set([i for i in range(n)])-cols_used
            
            for c in cols_possible:   
                if not check_possible_arrangement(rows, r, c):
                    continue
                    
                rows[r] = c
                recurse(r+1, n, rows)
               
            if r in rows:
                del rows[r]
            return
                
        recurse(0, n, {})
        return all_grids
