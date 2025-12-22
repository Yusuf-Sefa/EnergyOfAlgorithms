from codecarbon import EmissionsTracker
from Algorithms import BellmanFord, FloydWarshall, Knapsack
import random

'''
    There are three display functions. These functions can used to display any array
'''
def displayArray(arr):
    for i in range (len(arr)):
        print(arr[i] + " ")
def display2DArray(arr):
    for i in range (len(arr)):
        print()
        for j in range(len(arr[0])):
            print(arr[i][j] , end=" ")

'''
    There are three helper functions to create datasets of increasing complexity(Easy, middle, hard).
    Graph Data: Generates vertices (V), edges, and adjacency matrices for Shortest Path algorithms.
    Knapsack Data: Generates random weights, values, and maximum capacities for the Knapsack algorithm.
'''
def get_easy_data():
    V = 10
    edges = [[u, v, random.randint(1, 10)] for u in range(V) for v in range(V) if u != v][:20]
    matrix = [[0 if i == j else random.randint(1, 10) if random.random() > 0.7 else 100000000 for j in range(V)] for i in range(V)]
    
    weights = [random.randint(1, 20) for _ in range(50)]
    values = [random.randint(10, 100) for _ in range(50)]
    capacity = 100
    
    return V, edges, matrix, weights, values, capacity
def get_middle_data():
    V = 50
    edges = [[u, v, random.randint(1, 10)] for u in range(V) for v in range(V) if u != v][:250]
    matrix = [[0 if i == j else random.randint(1, 10) if random.random() > 0.5 else 100000000 for j in range(V)] for i in range(V)]
    
    weights = [random.randint(1, 50) for _ in range(200)]
    values = [random.randint(10, 200) for _ in range(200)]
    capacity = 1000
    
    return V, edges, matrix, weights, values, capacity
def get_hard_data():
    V = 200
    edges = [[u, v, random.randint(1, 10)] for u in range(V) for v in range(V) if u != v][:2000]
    matrix = [[0 if i == j else random.randint(1, 10) if random.random() > 0.3 else 100000000 for j in range(V)] for i in range(V)]
    
    weights = [random.randint(1, 100) for _ in range(1000)]
    values = [random.randint(10, 500) for _ in range(1000)]
    capacity = 5000
    
    return V, edges, matrix, weights, values, capacity

'''
    There are three "Test" functions for the energy emissions process(with "tracker" parameter).
    Functions contains for loops, 
    this loops run the algorithm multiple time (with "repeat" parameter) to get a significant measurement.
    TestBellmanford: Measures the Single-Source Shortest Path algorithm.
    TestFloydWarshall: Measures the All-Pairs Shortest Path algorithm.
    TestKnapsack: Measures the Dynamic Programming approach to the Knapsack problem.
'''
def TestBellmanford(V, source, edges, tracker, repeat):
    bf_obj = BellmanFord(V, source, edges)

    tracker.start()
    for _ in range(repeat):
        bf_obj.BellmanFordAlgorithm()
    tracker.stop()
def TestFloydWarshall(matrix, tracker, repeat):
    fw_obj = FloydWarshall(matrix)

    tracker.start()
    for _ in range(repeat):
        fw_obj.FloyWarshall()
    tracker.stop()
def TestKnapsack(weights, values, capacity, tracker, repeat):
    ks_obj = Knapsack(weights, values, capacity)

    tracker.start()
    for _ in range(repeat):
        ks_obj.Knapsack()
    tracker.stop()

if __name__ == '__main__':

    '''
        Initializations to datasets.
    '''
    Easy_V, Easy_edges, Easy_matrix , Easy_weights, Easy_values, Easy_capacity = get_easy_data()
    Mid_V, Mid_edges, Mid_matrix, Mid_weights, Mid_values, Mid_capacity = get_middle_data()
    Hard_V, Hard_edges, Hard_matrix, Hard_weights, Hard_values, Hard_capacity = get_hard_data()


    '''
        It creates individual EmissionsTracker instances for every algorithm and difficulty level
    '''
    BE_tracker = EmissionsTracker(project_name = "Bellman_Easy_Tracker")
    BM_tracker = EmissionsTracker(project_name = "Bellman_Mid_Tracker")
    BH_tracker = EmissionsTracker(project_name = "Bellman_Hard_Tracker")

    FE_tracker = EmissionsTracker(project_name = "Floyd_Easy_Tracker")
    FM_tracker = EmissionsTracker(project_name = "Floyd_Mid_Tracker")
    FH_tracker = EmissionsTracker(project_name = "Floyd_Hard_Tracker")

    KE_tracker = EmissionsTracker(project_name = "Knapsack_Easy_Tracker")
    KM_tracker = EmissionsTracker(project_name = "Knapsack_Mid_Tracker")
    KH_tracker = EmissionsTracker(project_name = "Knapsack_Hard_Tracker")


    '''
        The commented-out lines at the bottom are intended to execute the tests.
        They can be run in any desired order and parameters.
    '''
    #TestBellmanford(Easy_V, 0, Easy_edges, BE_tracker, 100000)
    #TestBellmanford(Mid_V, 0, Mid_edges, BM_tracker, 10000)
    #TestBellmanford(Hard_V, 0, Hard_edges, BH_tracker, 1000)

    #TestFloydWarshall(Easy_matrix, FE_tracker, 10000)
    #TestFloydWarshall(Mid_matrix, FM_tracker, 1000)
    #TestFloydWarshall(Hard_matrix, FH_tracker, 100)

    #TestKnapsack(Easy_weights, Easy_values, Easy_capacity, KE_tracker, 10000)
    #TestKnapsack(Mid_weights, Mid_values, Mid_capacity, KM_tracker, 1000)
    #TestKnapsack(Hard_weights, Hard_values, Hard_capacity, KH_tracker, 100)

