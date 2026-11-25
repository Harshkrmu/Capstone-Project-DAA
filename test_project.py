import unittest
from sorting import sort_parcels
from knapsack import knapsack
from dijkstra import build_graph, dijkstra
from tsp import nearest_neighbor_tsp


class CourierPlannerTests(unittest.TestCase):
    def setUp(self):
        self.parcels = [
            {"id":"x","destination":"A","weight":4,"value":10,"priority":1,"deadline":"2026-11-20"},
            {"id":"y","destination":"B","weight":3,"value":12,"priority":3,"deadline":"2026-11-21"},
            {"id":"z","destination":"C","weight":2,"value":8,"priority":3,"deadline":"2026-11-19"},
        ]

    def test_sorting(self):
        result = sort_parcels(self.parcels)
        self.assertEqual([p["id"] for p in result], ["z", "y", "x"])

    def test_knapsack_capacity(self):
        selected, weight, value, _ = knapsack(self.parcels, 5)
        self.assertLessEqual(weight, 5)
        self.assertEqual(value, 20)

    def test_dijkstra(self):
        graph = {"A":[("B",2)], "B":[("A",2),("C",3)], "C":[("B",3)]}
        distance, path = dijkstra(graph, "A", "C")
        self.assertEqual(distance, 5)
        self.assertEqual(path, ["A","B","C"])

    def test_tsp_starts_and_ends_at_depot(self):
        graph = {"D":[("A",1),("B",4)], "A":[("D",1),("B",2)], "B":[("D",4),("A",2)]}
        route, distance = nearest_neighbor_tsp(graph, "D", ["A","B"])
        self.assertEqual(route[0], "D")
        self.assertEqual(route[-1], "D")
        self.assertGreater(distance, 0)


if __name__ == "__main__":
    unittest.main()
