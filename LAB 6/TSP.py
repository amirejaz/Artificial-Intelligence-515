# program to implement traveling salesman
# problem using brute force approach.
from itertools import permutations

# Calculate the total cost of a given path in the graph
def path_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i+1]]
    cost += graph[path[-1]][path[0]]
    return cost

# Generate all possible permutations of paths and return the minimum cost path
def tsp(graph):
    n = len(graph)
    best_path = None
    best_cost = float('inf')
    for path in permutations(range(n)):
        cost = path_cost(graph, path)
        if cost < best_cost:
            best_path = path
            best_cost = cost
    return best_path, best_cost

# Driver Code
if __name__ == "__main__":
    # matrix representation of graph
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
             [15, 35, 0, 30], [20, 25, 30, 0]]

    # Compute the minimum cost path
    best_path, best_cost = tsp(graph)
    print("Best path: ", best_path)
    print("Best cost: ", best_cost)
