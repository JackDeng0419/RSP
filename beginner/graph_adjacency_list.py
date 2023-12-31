class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].remove(vertex2)
            self.adj_list[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for key in self.adj_list:
                if vertex in self.adj_list[key]:
                    self.adj_list[key].remove(vertex)
            del self.adj_list[vertex]

    def display(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

    def dfs(self, start):
        visited = {}
        for vertex in self.adj_list:
            visited[vertex] = False

        # create a stack
        stack = []
        stack.append(start)
        visited[start] = True

        while stack:
            vertex = stack.pop()
            print(vertex)
            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True

    def bfs(self, start):
        visited = {}
        for vertex in self.adj_list:
            visited[vertex] = False

        # create a queue
        queue = []
        queue.append(start)
        visited[start] = True

        while queue:
            vertex = queue.pop(0)
            print(vertex)
            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")
    graph.add_edge("D", "E")
    graph.add_edge("D", "F")
    graph.add_edge("E", "F")
    graph.display()
    print()

    print("DFS")
    graph.dfs("A")
    print()

    print("BFS")
    graph.bfs("A")
    print()

    graph.remove_vertex("E")
    graph.display()
    print()
    graph.remove_edge("A", "B")
    graph.display()
