''' question-8:-Write a function is_automorphic(n) that checks if a number's square ends with the number itself'''

import time
import tracemalloc

def is_automorphic(n):
    squared = n ** 2
    return str(squared).endswith(str(n))

num = 25

tracemalloc.start()
start_time = time.time()
result = is_automorphic(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024

print(f"n={num}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
