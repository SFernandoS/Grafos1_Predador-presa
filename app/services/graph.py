class GraphService:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        self.adj_list[v] = []

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):
        visited = {}
        for v in self.adj_list:
            visited[v] = False
        queue = [start]
        visited[start] = True
        while queue:
            current = queue.pop(0)
            print(current)
            for neighbor in self.adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
