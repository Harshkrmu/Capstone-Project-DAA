# Mini-Courier Planner – Capstone Report

**Course:** Design & Analysis of Algorithms (ETCCDA302)  
**Student Name:** ____________________  
**Roll Number:** ____________________  
**Programme/Semester:** B.Tech CSE & Specializations / __________  
**Faculty:** Dr. Shweta Agarwal  

## 1. Problem definition
The project simulates a courier planning system. It receives parcel records, a vehicle capacity, and a weighted road graph. It prioritizes parcels, chooses a high-value feasible parcel set, calculates shortest paths, and produces an approximate delivery tour.

## 2. Objectives
- Apply a sorting algorithm to parcel prioritization.
- Apply Dynamic Programming to the 0/1 Knapsack problem.
- Represent delivery locations as a weighted graph.
- Apply Dijkstra's shortest-path algorithm.
- Approximate a multi-stop delivery tour using Nearest Neighbor TSP.
- Measure runtime on datasets of increasing sizes.

## 3. System design
Input data is stored in JSON files. `main.py` coordinates the algorithm modules. The selected parcel destinations are passed to the graph-routing components. Performance measurements are written to CSV and, when Matplotlib is installed, a chart is generated.

## 4. Algorithm implementation
### 4.1 Merge Sort
Parcels are sorted by descending priority. If priorities are equal, the earlier deadline is placed first. Merge Sort divides the list, recursively sorts each half, and merges the sorted halves.

### 4.2 0/1 Knapsack using Dynamic Programming
The DP state `dp[i][c]` represents the maximum value achievable using the first `i` parcels with capacity `c`. For each parcel, the algorithm either excludes it or includes it if its weight fits. Backtracking identifies the selected parcels.

### 4.3 Dijkstra's Algorithm
The road network is an adjacency-list graph. A min-heap selects the currently closest unprocessed node. Distances are relaxed until the shortest distance to the target is finalized. All edge weights must be non-negative.

### 4.4 Nearest Neighbor TSP Approximation
Starting at the depot, the algorithm repeatedly chooses the nearest unvisited destination. Distance between two stops is calculated using Dijkstra. After all destinations are visited, the route returns to the depot. This is a heuristic and may not produce the globally shortest tour.

## 5. Test data and test cases
The supplied sample data contains seven parcels, six graph nodes including the depot, and twelve undirected roads. The default vehicle capacity is 25 kg.

| Test | Input | Expected check |
|---|---|---|
| 1 | Sample parcel dataset | Output is sorted by priority and deadline |
| 2 | Capacity 25 kg | Selected parcel weight does not exceed 25 kg |
| 3 | Connected road graph | Dijkstra returns a route and finite distance |
| 4 | Selected destinations | TSP route starts and ends at depot |
| 5 | Dataset sizes 10, 30, 60, 100 | Runtime CSV contains one row per size |

**Actual results:** Run the application and paste the observed output and measured runtimes here. Do not invent benchmark values.

## 6. Complexity analysis

| Algorithm | Time complexity | Space complexity |
|---|---:|---:|
| Merge Sort | O(n log n) | O(n) |
| 0/1 Knapsack DP | O(nW) | O(nW) |
| Dijkstra with heap | O((V+E) log V) | O(V+E) |
| Nearest Neighbor with Dijkstra distances | Repeated shortest-path computations; see README | O(V+E+k) |

## 7. Limitations
The road graph and parcel data are sample data. Knapsack maximizes a numeric value score, not deadline compliance directly. Nearest Neighbor is approximate. The prototype uses one vehicle and one trip.

## 8. Conclusion
The project demonstrates how sorting, Dynamic Programming, graph shortest paths, and approximation techniques can be integrated into a single courier-planning workflow. The program produces a parcel selection, shortest-path information, a delivery sequence, and runtime measurements.

## 9. Evidence to attach
Insert:
1. Screenshot of program execution.
2. Screenshot of sorted parcel list and packing result.
3. Screenshot of Dijkstra paths and final TSP route.
4. Runtime CSV/chart.
5. Any additional test cases run by the student.
