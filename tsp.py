from dijkstra import dijkstra


def nearest_neighbor_tsp(graph, start, destinations):
    """
    Approximate a delivery tour using nearest-neighbor selection.
    Distances between stops are shortest-path distances from Dijkstra.
    Returns route (including return to depot) and total distance.
    """
    remaining = set(destinations)
    remaining.discard(start)
    route = [start]
    current = start
    total_distance = 0

    while remaining:
        candidates = []
        for destination in remaining:
            distance, _ = dijkstra(graph, current, destination)
            candidates.append((distance, destination))
        distance, next_stop = min(candidates)
        if distance == float("inf"):
            raise ValueError(f"No route from {current} to any remaining destination.")
        total_distance += distance
        route.append(next_stop)
        remaining.remove(next_stop)
        current = next_stop

    if current != start:
        distance, _ = dijkstra(graph, current, start)
        if distance == float("inf"):
            raise ValueError("No route back to depot.")
        total_distance += distance
        route.append(start)

    return route, total_distance
