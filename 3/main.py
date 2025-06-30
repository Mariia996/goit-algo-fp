import heapq

class Graph:
    """Клас для представлення неорієнтованого графа з використанням списків суміжності."""
    def __init__(self):
        self.graph = {}

    def add_edge(self, from_t: str, to_t: str, weight: int):
        """Додає ребро до графа."""
        if from_t not in self.graph:
            self.graph[from_t] = []
        if to_t not in self.graph:
            self.graph[to_t] = []
        self.graph[from_t].append((to_t, weight))
        self.graph[to_t].append((from_t, weight))

    def dijkstra(self, start: str):
        """Виконує алгоритм Дейкстри для знаходження найкоротших шляхів від початкової вершини."""
        min_heap = []
        heapq.heappush(min_heap, (0, start))
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        prev_nodes = {node: None for node in self.graph}
        visited = set()
        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)
            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))
        return distances, prev_nodes

def reconstruct_path(prev_nodes, start: str, end: str):
    """Відновлює шлях від початкової вершини до кінцевої на основі попередніх вузлів."""
    path = []
    current = end
    while current:
        path.append(current)
        current = prev_nodes[current]
    path.reverse()
    return path if path[0] == start else []

def main():
    g = Graph()
    g.add_edge("A", "B", 6)
    g.add_edge("B", "C", 4)
    g.add_edge("C", "D", 5)
    g.add_edge("D", "E", 7)
    g.add_edge("E", "F", 3)
    g.add_edge("B", "E", 8)
    g.add_edge("A", "F", 12)

    start_node = 'A'
    distances, prev = g.dijkstra(start_node)

    print(f"Найкоротші шляхи від вершини {start_node}:")
    for node, distance in distances.items():
        path = reconstruct_path(prev, start_node, node)
        print(f"До {node}:  шлях {path} з довжиною {distance}")
if __name__ == "__main__":
    main()

# Найкоротші шляхи від вершини A:
# До A:  шлях ['A'] з довжиною 0
# До B:  шлях [] з довжиною 6
# До C:  шлях [] з довжиною 10
# До D:  шлях [] з довжиною 15
# До E:  шлях [] з довжиною 14
# До F:  шлях [] з довжиною 12