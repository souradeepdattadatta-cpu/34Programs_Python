''' question-18:- Write a function multiplicative_persistence(n) that counts how many steps until a number's digits multiply to a single digit.'''

import time
import tracemalloc

def multiplicative_persistence(n):
    steps = 0
    while n >= 10:
        product = 1
        for d in str(n):
            product *= int(d)
        n = product
        steps += 1
    return steps

num = 39  # Example input

tracemalloc.start()
start_time = time.time()
result = multiplicative_persistence(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024  # in KB

print(f"n={num}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
