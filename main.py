from sorting import sort_parcels
from knapsack import knapsack
from dijkstra import build_graph, dijkstra
from tsp import nearest_neighbor_tsp
from performance import run_benchmarks
from data_io import load_json
from pathlib import Path


def print_parcels(parcels):
    print("\nPARCELS (sorted by priority, then earliest deadline)")
    print("-" * 65)
    print(f"{'ID':<8}{'Destination':<18}{'Weight':>9}{'Value':>9}{'Priority':>11}{'Deadline':>12}")
    for p in parcels:
        print(f"{p['id']:<8}{p['destination']:<18}{p['weight']:>9}{p['value']:>9}{p['priority']:>11}{p['deadline']:>12}")


def main():
    root = Path(__file__).resolve().parent
    parcels = load_json(root / "data" / "parcels.json")
    locations = load_json(root / "data" / "locations.json")
    capacity = 25
    depot = "DEPOT"

    sorted_parcels = sort_parcels(parcels)
    print("=" * 65)
    print("                 MINI-COURIER PLANNER")
    print("=" * 65)
    print(f"Vehicle capacity: {capacity} kg | Starting point: {depot}")
    print_parcels(sorted_parcels)

    chosen, total_weight, total_value, dp = knapsack(sorted_parcels, capacity)
    print("\nOPTIMAL PACKING PLAN (0/1 KNAPSACK)")
    print("-" * 65)
    print("Selected parcels:", ", ".join(p["id"] for p in chosen) or "None")
    print(f"Total weight: {total_weight} / {capacity} kg")
    print(f"Total delivery value: {total_value}")

    graph = build_graph(locations)
    destinations = list(dict.fromkeys(p["destination"] for p in chosen))
    print("\nSHORTEST PATHS FROM DEPOT (DIJKSTRA)")
    print("-" * 65)
    for destination in destinations:
        distance, path = dijkstra(graph, depot, destination)
        print(f"{depot} -> {destination}: {distance} km | Path: {' -> '.join(path)}")

    route, route_distance = nearest_neighbor_tsp(graph, depot, destinations)
    print("\nDELIVERY ROUTE (NEAREST NEIGHBOR TSP APPROXIMATION)")
    print("-" * 65)
    print(" -> ".join(route))
    print(f"Estimated route distance: {route_distance} km")
    print("\nNOTE: Nearest Neighbor is a heuristic; it does not guarantee the globally shortest TSP tour.")

    print("\nPERFORMANCE TESTING")
    print("-" * 65)
    results = run_benchmarks()
    for row in results:
        print(f"{row['n']:>5} parcels | sorting: {row['sorting_ms']:.4f} ms | knapsack: {row['knapsack_ms']:.4f} ms")
    print("\nBenchmark data saved to results/runtime_results.csv")
    print("If matplotlib is installed, results/runtime_chart.png is also generated.")
    print("\nProject run completed successfully.")


if __name__ == "__main__":
    main()
