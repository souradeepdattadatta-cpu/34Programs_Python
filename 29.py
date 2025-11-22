'''question-29:- Write a function Polygonal Numbers polygonal_number(s, n) that returns the n-th s-gonal number.'''

import time
import tracemalloc

def polygonal_number(s, n):
    if s < 3 or n < 1:
        return None
    return ((s - 2) * n * (n - 1)) // 2 + n

s = 5  # Example: pentagonal numbers
n = 10  # Example input

tracemalloc.start()
start_time = time.time()
result = polygonal_number(s, n)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024  # in KB

print(f"s={s}, n={n}, polygonal_number={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
