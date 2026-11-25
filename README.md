# Mini-Courier Planner

A Python capstone prototype integrating sorting, Dynamic Programming, graph algorithms, TSP approximation, and runtime testing.

## Requirements
- Python 3.9 or newer
- Optional: Matplotlib for runtime chart generation

## Setup and run

Open a terminal in this folder:

```bash
python main.py
```

To generate the runtime chart, install the optional dependency first:

```bash
python -m pip install -r requirements.txt
python main.py
```

The program writes:
- `results/runtime_results.csv`
- `results/runtime_chart.svg` (generated without extra dependencies)
- `results/runtime_chart.png` (also generated when Matplotlib is installed)

## Project workflow
1. Merge Sort prioritizes parcels by descending priority, then ascending deadline.
2. 0/1 Knapsack uses parcel `value` as the objective and `weight` as the capacity cost.
3. Dijkstra computes shortest paths in the undirected road graph.
4. Nearest Neighbor TSP repeatedly visits the nearest unvisited delivery destination, using Dijkstra distances, then returns to the depot.
5. Performance testing measures Merge Sort and Knapsack on increasing synthetic parcel datasets.

## Data format

Each parcel contains:
- `id`: unique parcel identifier
- `destination`: graph node for delivery
- `weight`: integer weight
- `value`: integer benefit/importance score used by Knapsack
- `priority`: integer sorting priority (higher is more urgent)
- `deadline`: ISO date string (`YYYY-MM-DD`)

The locations file contains nodes and weighted road edges. Distances must be non-negative.

## Algorithms and complexity

| Component | Algorithm | Time complexity | Auxiliary space |
|---|---|---:|---:|
| Prioritization | Merge Sort | O(n log n) | O(n) |
| Packing | 0/1 Knapsack DP | O(nW) | O(nW) |
| Shortest path | Dijkstra with binary heap | O((V+E) log V) | O(V+E) |
| Delivery order | Nearest Neighbor TSP using shortest-path queries | O(k(V+E) log V + k² log k) upper-bound style | O(V+E+k) |
| Benchmark | `perf_counter` | Depends on tested algorithms | Depends on algorithms |

`n` = number of parcels, `W` = integer vehicle capacity, `V` = graph vertices, `E` = graph edges, `k` = unique delivery destinations.

## Assumptions and limitations
- The vehicle capacity is set to 25 kg in `main.py`.
- Parcel `value` is a demonstration score, not actual revenue.
- The selected parcel set is optimized for total value under the capacity constraint.
- The TSP routine is a heuristic and does not guarantee the globally optimal tour.
- The route planner visits each selected destination once. Multiple parcels at one destination are grouped into one stop.
- The graph is an illustrative undirected road network; replace it with real map distances for a real deployment.
- Runtime measurements vary by computer and should be recorded from the machine used for submission.

## Suggested extensions
- Read vehicle capacity from user input.
- Add a menu and input validation.
- Compare Merge Sort with another sorting algorithm.
- Compare nearest-neighbor route with exact TSP for very small graphs.
- Add real road data and multiple vehicles.

## Submission checklist
- [ ] Run `python main.py` and verify the output.
- [ ] Keep screenshots of the complete terminal output.
- [ ] Include `results/runtime_results.csv`.
- [ ] Include `results/runtime_chart.png` if Matplotlib is installed.
- [ ] Read the code and prepare to explain each algorithm.
- [ ] Update this README with your name, roll number, course section, and actual test observations.
