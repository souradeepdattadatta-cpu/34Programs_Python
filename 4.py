''' question-4:- Write a function digital_root(n) that repeatedly sums the digits of a number until a single digit is obtained.'''

import time
import tracemalloc

def digital_root(n):
    while n > 9:
        digits = [int(d) for d in str(n)]
        n = sum(digits)
    return n

num = 493193

tracemalloc.start()
start_time = time.time()
result = digital_root(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024

print(f"n={num}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")


