''' question-5:- Write a function is_abundant(n) that returns True if the sum of proper divisors of n is greater than n.'''

import time
import tracemalloc

def is_abundant(n):
    if n < 12:
        return False
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum > n

num = 18

tracemalloc.start()
start_time = time.time()
result = is_abundant(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak/1024

print(f"n={num}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
