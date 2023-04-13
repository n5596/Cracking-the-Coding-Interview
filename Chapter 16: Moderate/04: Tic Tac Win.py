class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        grid = [['' for j in range(3)] for i in range(3)]
        
        def get_pinfo(i):
            if i % 2 == 0: 
                return "A", "X"
            return "B", "O"
        
        def check_move(r, c, pchar):
            grid[move[0]][move[1]] = pchar
            flag1, flag2, flag3 = True, True, True
            
            for j in range(3): # check rows
                if grid[r][j] != pchar:
                    flag1 = False
                    break
            
            for i in range(3): # check cols
                if grid[i][c] != pchar:
                    flag2 = False
                    break
                
            # check diagonals
            if (grid[0][0] != pchar or grid[1][1] != pchar or grid[2][2] != pchar) and (grid[0][2] != pchar or grid[1][1] != pchar or grid[2][0] != pchar):
                flag3 = False
                
            return flag1|flag2|flag3
        
        for i in range(len(moves)):
            move = moves[i]
            player, pchar = get_pinfo(i)
            if check_move(move[0], move[1], pchar):
                return player
            
        if len(moves) == 9:
            return "Draw"
        return "Pending"
