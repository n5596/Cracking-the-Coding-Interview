class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {}
                            
        def add_edge(u, v): # v depends on u
            glist = graph.get(u, [])
            glist.append(v)
            graph[u] = glist
                        
        for p in prerequisites:
            add_edge(p[1], p[0])
            
        order = []
        vis = [0]*numCourses  # 0: unvisited, 1: partial, 2: fully processed
        
        def recurse(node):
            vis[node] = 1 # partial
            
            if node not in graph: # no course depends on this one
                order.append(node)
                vis[node] = 2
                return True            
            
            for neighbor in graph[node]:
                if vis[neighbor] == 1: # revisiting a partially processed node so there is a cycle. ABORT!
                    return False
                
                if vis[neighbor] == 2: # already processed
                    continue
                
                flag = recurse(neighbor)
                if flag == False:
                    return False
                
            order.append(node) # add it after processing all children nodes
            vis[node] = 2
            return True
        
        print(graph)
        
        for i in range(numCourses):
            if vis[i] == 0:
                flag = recurse(i)
                
                if flag == False:
                    return []
        return order[::-1]
