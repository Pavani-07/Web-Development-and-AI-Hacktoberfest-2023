from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node, to_node)]

def ucs(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, [start]))

    while not queue.empty():
        cost, path = queue.get()
        node = path[-1]
        if node not in visited:
            visited.add(node)

            if node == goal:
                return cost, path  # Return the cost of reaching the goal and its path
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    total_cost = cost + graph.get_cost(node, neighbor)
                    new_path = path + [neighbor]
                    queue.put((total_cost, new_path))


# A graph example
g = Graph()
g.edges = {
    'S': ['A', 'B', 'C'],
    'A': ['D'],
    'B': ['E'],
    'C': ['G'],
    'D': ['F'],
    'F': ['G'],
    'E': ['G']
}

g.weights = {
    ('S', 'A'): 3,
    ('S', 'B'): 2,
    ('S', 'C'): 1,
    ('A', 'D'): 6,
    ('B', 'E'): 4,
    ('C', 'G'): 20,
    ('D', 'F'): 1,
    ('F', 'G'): 1,
    ('E', 'G'): 8
}

start_node = 'S'
goal_node = 'G'
cost, path = ucs(g, start_node, goal_node)
print("Shortest path cost:", cost)
print("Shortest path:", "->".join(path))
