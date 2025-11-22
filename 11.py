'''question-11:- Write a function count_distinct_prime_factors(n) that returns how many unique prime factors a number has.'''

import time
import tracemalloc

def count_distinct_prime_factors(n):
    distinct_factors = set()
    while n % 2 == 0:
        distinct_factors.add(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            distinct_factors.add(i)
            n //= i
    if n > 2:
        distinct_factors.add(n)
    return len(distinct_factors)

num = 360  # Example input

tracemalloc.start()
start_time = time.time()
result = count_distinct_prime_factors(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024  # in KB

print(f"n={num}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
