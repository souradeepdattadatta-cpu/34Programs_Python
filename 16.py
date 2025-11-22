'''question-16:-Write a function aliquot_sum(n) that returns the sum of all proper divisors of n (divisors less than n).'''

import time
import tracemalloc

def aliquot_sum(n):
    if n <= 1:
        return 0
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

num = 28  # Example input

tracemalloc.start()
start_time = time.time()
result = aliquot_sum(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024  # in KB

print(f"n={num}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
