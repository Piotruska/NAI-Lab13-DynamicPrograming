import time
from Task1 import knapsack_recursive
from Task2 import knapsack_memoization
from Task3 import knapsack_dp


def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start

# Test cases
weights = [3, 1, 6, 10, 1, 4, 9, 1, 7, 2, 6, 1, 6, 2, 2, 4, 8, 1, 7, 3, 6, 2, 9, 5, 3, 3, 4, 7, 3, 5, 30, 50]
values = [7, 4, 9, 18, 9, 15, 4, 2, 6, 13, 18, 12, 12, 16, 19, 19, 10, 16, 14, 3, 14, 4, 15, 7, 5, 10, 10, 13, 19, 9, 8, 5]
n = 32
W = 75

# Measure time for recursive approach
result_recursive, time_recursive = measure_time(knapsack_recursive, weights, values, n, W)
print(f"Recursive: Result = {result_recursive}, Time = {time_recursive:.6f} seconds")

# Measure time for memoization approach
result_memoization, time_memoization = measure_time(knapsack_memoization, weights, values, n, W)
print(f"Memoization: Result = {result_memoization}, Time = {time_memoization:.6f} seconds")

# Measure time for dynamic programming approach
result_dp, time_dp = measure_time(knapsack_dp, weights, values, n, W)
print(f"Dynamic Programming: Result = {result_dp}, Time = {time_dp:.6f} seconds")
