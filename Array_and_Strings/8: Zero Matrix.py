class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0])
        
        def add_zero(i, j):
            # store row info in first col
            matrix[i][0] = 0
            # store col info in first row
            matrix[0][j] = 0
            return
        
        def set_row_zero(r, idx, n):
            for j in range(idx, n):
                matrix[r][j] = 0
            return
        
        def set_col_zero(c, idx, m):
            for i in range(idx, m):
                matrix[i][c] = 0
            return
        
        rflag, cflag = False, False
        
        for i in range(m):
            if matrix[i][0] == 0:
                cflag = True
                break
                
        for j in range(n):
            if matrix[0][j] == 0:
                rflag = True
                break
                
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    add_zero(i, j)
              
        for i in range(1, m):
            if matrix[i][0] == 0:
                set_row_zero(i, 1, n)
    
        for j in range(1, n):
            if matrix[0][j] == 0:
                set_col_zero(j, 1, m)
                
        if rflag:
            set_row_zero(0, 0, n)
        if cflag:
            set_col_zero(0, 0, m)
