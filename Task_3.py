import heapq


Graph = dict[str, list[tuple[str, int]]]


def dijkstra(graph: Graph, start: str) -> dict[str, float]:
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    return distances


if __name__ == "__main__":
    graph: Graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2)],
        "E": [("C", 10), ("D", 2)]
    }

    start_vertex = "A"
    shortest_distances = dijkstra(graph, start_vertex)

    print(f"Найкоротші відстані від вершини {start_vertex}:")

    for vertex, distance in shortest_distances.items():
        print(f"До вершини {vertex}: {distance}")