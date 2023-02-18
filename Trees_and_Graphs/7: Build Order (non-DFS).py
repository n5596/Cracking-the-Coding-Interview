class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {}
        incoming = [0]*numCourses
        have_dependencies = set()
        
        def add_edge(u, v):
            glist = graph.get(u, [])
            glist.append(v)
            graph[u] = glist
        
        for p in prerequisites:
            add_edge(p[1], p[0])
            incoming[p[0]] += 1
            have_dependencies.add(p[0])
            
        all_nodes = set([i for i in range(numCourses)])
        independent = all_nodes-have_dependencies
        
        queue = collections.deque([])
        for course in independent:
            queue.append(course)
            
        order = []
        
        while len(queue) > 0:
            node = queue.popleft()
            order.append(node)
        
            if node not in graph:
                continue
                
            for neighbor in graph[node]:
                incoming[neighbor] -= 1
                
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
            
        if len(order) != numCourses: # cycle
            return []
        return order
