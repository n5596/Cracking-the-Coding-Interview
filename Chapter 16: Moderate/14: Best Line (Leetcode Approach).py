# Looked at the Leetcode solution
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        n = len(points)

        max_count = 1
        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            slopes = {}
            
            for j in range(n):
                if j == i:
                    continue
                    
                x2, y2 = points[j][0], points[j][1]
                angle = math.atan2(x1-x2, y1-y2)
                slopes[angle] = slopes.get(angle, 0)+1
                
            for k in slopes.keys():
                max_count = max(max_count, slopes[k]+1)
        
        return max_count
