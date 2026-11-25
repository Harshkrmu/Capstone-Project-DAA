import csv
import random
import time
from pathlib import Path
from sorting import sort_parcels
from knapsack import knapsack


def _make_dataset(n, seed=42):
    rng = random.Random(seed + n)
    parcels = []
    for i in range(n):
        parcels.append({
            "id": f"P{i}",
            "destination": "D1",
            "weight": rng.randint(1, 10),
            "value": rng.randint(10, 100),
            "priority": rng.randint(1, 5),
            "deadline": f"2026-12-{rng.randint(1, 28):02d}"
        })
    return parcels


def run_benchmarks(sizes=(10, 30, 60, 100)):
    """Measure sorting and knapsack on reproducible generated datasets."""
    project_root = Path(__file__).resolve().parent
    results_dir = project_root / "results"
    results_dir.mkdir(exist_ok=True)
    rows = []

    for n in sizes:
        data = _make_dataset(n)
        start = time.perf_counter()
        sorted_data = sort_parcels(data)
        sorting_ms = (time.perf_counter() - start) * 1000

        start = time.perf_counter()
        knapsack(sorted_data, 25)
        knapsack_ms = (time.perf_counter() - start) * 1000

        rows.append({
            "n": n,
            "sorting_ms": sorting_ms,
            "knapsack_ms": knapsack_ms
        })

    csv_path = results_dir / "runtime_results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["n", "sorting_ms", "knapsack_ms"])
        writer.writeheader()
        writer.writerows(rows)

    try:
        import matplotlib.pyplot as plt
        sizes = [r["n"] for r in rows]
        plt.figure()
        plt.plot(sizes, [r["sorting_ms"] for r in rows], marker="o", label="Merge Sort")
        plt.plot(sizes, [r["knapsack_ms"] for r in rows], marker="o", label="0/1 Knapsack DP")
        plt.xlabel("Number of parcels")
        plt.ylabel("Runtime (milliseconds)")
        plt.title("Mini-Courier Planner: Runtime Comparison")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(results_dir / "runtime_chart.png", dpi=160)
        plt.close()
    except ImportError:
        pass

    return rows
