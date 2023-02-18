class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = {}
        
        def add_edge(u, v):
            glist = graph.get(u, [])
            glist.append(v)
            graph[u] = glist
            
        for e in edges:
            add_edge(e[0], e[1])
            add_edge(e[1], e[0])
            
        queue = collections.deque([])
        queue.append(source)
        
        vis = set()
        
        while len(queue) > 0:
            node = queue.popleft()
            vis.add(node)
            
            if node == destination:
                return True
            
            if node not in graph:
                return False
            
            for neighbor in graph[node]:
                if neighbor not in vis:
                    queue.append(neighbor)
                    vis.add(neighbor)
                    
        return False
