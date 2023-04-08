class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        records = {}
        
        for person in logs:
            birth, death = person[0], person[1]
            records[birth] = records.get(birth, 0)+1
            records[death] = records.get(death,0)-1 # have to use death instead of (death+1) as person is not counted in death year according to the problem description
            
        max_alive_year = 0
        max_alive_count = -1
        
        curr_alive = 0
        
        for key in sorted(records.keys()):
            curr_alive += records[key]
            
            if max_alive_count < curr_alive:
                max_alive_year = key
                max_alive_count = curr_alive
                
        return max_alive_year
