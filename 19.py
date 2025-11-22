''' question-19:- Write a function is_highly_composite(n) that checks if a number has more divisors than any smaller number'''

import time
import tracemalloc

def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count

def is_highly_composite(n):
    divisors_n = count_divisors(n)
    for i in range(1, n):
        if count_divisors(i) >= divisors_n:
            return False
    return True

num = 12  # Example input

tracemalloc.start()
start_time = time.time()
result = is_highly_composite(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024  # in KB

print(f"n={num}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
