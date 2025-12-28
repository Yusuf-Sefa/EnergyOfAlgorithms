# EnergyOfAlgorithms
**Dynamic Programming Algorithms
**
Dynamic programming is a method that solves complex problems by breaking them down into smaller subproblems,

and prevents recalculation by storing the results of these subproblems (Bellman, 1957). This approach is frequently used, especially in optimization problems.
Bellman-Ford Algorithm: This algorithm, developed by Richard Bellman (1958) and Lester Ford, solves the shortest path problem from a single source in graphs containing negatively weighted edges. The time complexity of the algorithm is O(VE); where V represents the number of nodes and E represents the number of edges. Unlike the Dijkstra algorithm, it has the ability to handle negatively weighted edges as well (Cormen et al., 2009).
Floyd-Warshall Algorithm: Developed independently by Robert Floyd (1962) and Stephen Warshall (1962), this algorithm calculates the shortest paths between all pairs of nodes in a graph. The algorithm has a time complexity of O(V³) and offers an efficient solution for the all pairs problem thanks to its dynamic programming-based structure.

It can be practically used for small and medium-sized graphs.
0-1 Knapsack Problem: The knapsack problem is a classic problem in the field of combinatorial optimization (Dantzig, 1957). The problem aims to obtain the maximum value from items with specific weights and values ​​such that the total weight does not exceed the capacity. With the dynamic programming approach, it can be solved in pseudo-polynomial time of O(nW); where n is the number of items and W is the maximum value of the capacity (Martello and Toth, 1990).

