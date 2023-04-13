class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def recurse(r, c, ocolor, ncolor):
            if r < 0 or c < 0  or r >= len(image) or c >= len(image[0]):
                return
            
            if image[r][c] != ocolor:
                return 
            
            image[r][c] = ncolor
            
            recurse(r-1, c, ocolor, ncolor)
            recurse(r, c-1, ocolor, ncolor)
            recurse(r+1, c, ocolor, ncolor)
            recurse(r, c+1, ocolor, ncolor)
            return
        
        if image[sr][sc] != color:
            recurse(sr, sc, image[sr][sc], color)
        return image
