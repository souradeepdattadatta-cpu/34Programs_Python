'''question-27:-Write a function for Perfect Powers Check is_perfect_power(n) that checks if a number can be expressed as aᵇ where a > 0 and b > 1.'''

import time
import tracemalloc
import math

def is_perfect_power(n):
    if n <= 1:
        return True
    for b in range(2, int(math.log2(n)) + 2):
        a = round(n ** (1 / b))
        if a > 1 and a ** b == n:
            return True
    return False

num = 81  # Example input

tracemalloc.start()
start_time = time.time()
result = is_perfect_power(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024  # in KB

print(f"n={num}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
