'''question-17:- Write a function are_amicable(a, b) that checks if two numbers are amicable (sum of proper divisors of a equals b and vice versa).'''

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

def are_amicable(a, b):
    return aliquot_sum(a) == b and aliquot_sum(b) == a

a = 220  # Example input
b = 284

tracemalloc.start()
start_time = time.time()
result = are_amicable(a, b)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024  # in KB

print(f"a={a}, b={b}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
