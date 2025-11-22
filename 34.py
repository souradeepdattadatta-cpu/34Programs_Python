''' question-34:- Write a function Partition Function p(n) partition_function(n) that calculates the number of distinct ways to write n as a sum of positive integers'''

import time
import tracemalloc

# Using a dynamic programming approach to calculate partition function p(n)
def partition_function(n):
    partitions = [0] * (n + 1)
    partitions[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]
    return partitions[n]

num = 50  # Example input

tracemalloc.start()
start_time = time.time()
result = partition_function(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"n={num}, partition_function={result}, time_taken_sec={end_time - start_time:.8f}, memory_utilized_KB={peak / 1024:.3f}")
