'''question-9:- write a function is_pronic(n) that checks if a number is the product of two consecutive integers.'''

import time
import tracemalloc
import math

def is_pronic(n):
    x = int(math.sqrt(n))
    return x * (x + 1) == n

num = 56  # Example input

tracemalloc.start()
start_time = time.time()
result = is_pronic(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024  # in KB

print(f"n={num}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
