# Practical 4: Uniform Cost Search on Romania Map
import heapq

ROMANIA_MAP = {
    "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Zerind": [("Arad", 75), ("Oradea", 71)],
    "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    "Timisoara": [("Arad", 118), ("Lugoj", 111)],
    "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
    "Mehadia": [("Lugoj", 70), ("Drobeta", 75)],
    "Drobeta": [("Mehadia", 75), ("Craiova", 120)],
    "Craiova": [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Rimnicu Vilcea": [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)],
    "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
    "Pitesti": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
    "Bucharest": [("Fagaras", 211), ("Pitesti", 101)],
}


def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        cost, current_node, path = heapq.heappop(priority_queue)

        if current_node == goal:
            return path, cost

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, edge_cost in graph.get(current_node, []):
            if neighbor not in visited:
                total_cost = cost + edge_cost
                heapq.heappush(priority_queue, (total_cost, neighbor, path + [neighbor]))

    return None, float('inf')


start_city = "Arad"
goal_city = "Bucharest"
optimal_path, total_cost = uniform_cost_search(ROMANIA_MAP, start_city, goal_city)
print("Optimal path:", optimal_path)
print("Total distance:", total_cost)
