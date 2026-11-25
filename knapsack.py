def knapsack(parcels, capacity):
    """
    0/1 Knapsack using bottom-up dynamic programming.
    Each parcel can be selected at most once.
    Maximizes total value without exceeding vehicle capacity.
    Returns selected parcels, total weight, total value, and DP table.
    """
    n = len(parcels)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = parcels[i - 1]["weight"]
        value = parcels[i - 1]["value"]
        for cap in range(capacity + 1):
            dp[i][cap] = dp[i - 1][cap]
            if weight <= cap:
                dp[i][cap] = max(
                    dp[i][cap],
                    value + dp[i - 1][cap - weight]
                )

    selected = []
    cap = capacity
    for i in range(n, 0, -1):
        if dp[i][cap] != dp[i - 1][cap]:
            parcel = parcels[i - 1]
            selected.append(parcel)
            cap -= parcel["weight"]

    selected.reverse()
    total_weight = sum(p["weight"] for p in selected)
    total_value = sum(p["value"] for p in selected)
    return selected, total_weight, total_value, dp
