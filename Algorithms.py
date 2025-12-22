
'''
    Class based implementation of algorithms(BellmanFord, FloydWarshall, Knapsack)
'''

class BellmanFord:
    def __init__(self, V, source, edges ):
        self.V = V
        self.source = source
        self.edges = edges
    
    def BellmanFordAlgorithm(self):
        V = self.V
        source = self.source
        edges = self.edges

        dist = [100000000] * V
        dist[source] = 0

        for i in range(V):
            for edge in edges:
                u, v, wt = edge
                if dist[u] != 100000000 and dist[u] + wt < dist[v]:
                    
                    if i == V - 1:
                        return [-1]
                    
                    dist[v] = dist[u] + wt
        return dist

class FloydWarshall:
    def __init__(self, distance):
        self.distance = distance

    def  FloyWarshall(self):
        distance = self.distance
        V = len(distance)

        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if(distance[i][k] != 100000000 and distance[k][j]!= 100000000):
                        distance[i][j] = min(distance[i][j],distance[i][k] + distance[k][j]);
        
        return distance
    
class Knapsack:
    def __init__(self, weights, values, capacity):
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.n = len(values)

    def Knapsack(self):
        dp = [[0 for _ in range(self.capacity + 1)] for _ in range(self.n + 1)]

        for i in range(1, self.n + 1):
            for w in range(1, self.capacity + 1):
                if self.weights[i-1] <= w:
                    dp[i][w] = max(self.values[i-1] + dp[i-1][w - self.weights[i-1]], dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]
        return dp[self.n][self.capacity]