'''question-13:-Write a function is_mersenne_prime(p) that checks if 2ᵖ - 1 is a prime number (given that p is prime).'''

import time
import tracemalloc

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_mersenne_prime(p):
    if not is_prime(p):
        return False
    m = (2 ** p) - 1
    return is_prime(m)

p = 7  # Example input

tracemalloc.start()
start_time = time.time()
result = is_mersenne_prime(p)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024  # in KB

print(f"p={p}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
