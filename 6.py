'''question-6:-Write a function is_deficient(n) that returns True if the sum of proper divisors of n is less than n.'''

import time
import tracemalloc

def is_deficient(n):
    if n <= 1:
        return True
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum < n

num = 15

tracemalloc.start()
start_time = time.time()
result = is_deficient(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024  # in KB

print(f"n={num}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
