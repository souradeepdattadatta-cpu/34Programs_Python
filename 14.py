'''question-14:-Write a function twin_primes(limit) that generates all twin prime pairs up to a given limit.'''

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

def twin_primes(limit):
    twins = []
    for num in range(2, limit - 1):
        if is_prime(num) and is_prime(num + 2):
            twins.append((num, num + 2))
    return twins

limit = 100  # Example input

tracemalloc.start()
start_time = time.time()
result = twin_primes(limit)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024  # in KB

print(f"limit={limit}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
