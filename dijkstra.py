import heapq


def build_graph(locations):
    """Build an undirected weighted adjacency-list graph from edge records."""
    graph = {}
    for edge in locations["edges"]:
        a, b, distance = edge["from"], edge["to"], edge["distance"]
        if distance < 0:
            raise ValueError("Dijkstra's algorithm requires non-negative edge weights.")
        graph.setdefault(a, []).append((b, distance))
        graph.setdefault(b, []).append((a, distance))
    return graph


def dijkstra(graph, start, target):
    """Return shortest distance and path from start to target."""
    if start not in graph or target not in graph:
        raise ValueError(f"Unknown graph node: {start if start not in graph else target}")

    distances = {node: float("inf") for node in graph}
    previous = {}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_distance, node = heapq.heappop(heap)
        if current_distance != distances[node]:
            continue
        if node == target:
            break

        for neighbor, weight in graph[node]:
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = node
                heapq.heappush(heap, (new_distance, neighbor))

    if distances[target] == float("inf"):
        return float("inf"), []

    path = []
    node = target
    while node != start:
        path.append(node)
        node = previous[node]
    path.append(start)
    path.reverse()
    return distances[target], path
