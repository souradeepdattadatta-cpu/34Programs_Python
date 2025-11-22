'''question-12:- Write a function is_prime_power(n) that checks if a number can be expressed as pᵏ where p is prime and k ≥ 1.'''

import time
import tracemalloc
import math

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

def is_prime_power(n):
    if n <= 1:
        return False
    for k in range(1, int(math.log2(n)) + 2):
        p = round(n ** (1/k))
        # Check if p^k matches n and p is prime
        if p**k == n and is_prime(p):
            return True
    return False

num = 27  # Example input

tracemalloc.start()
start_time = time.time()
result = is_prime_power(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024  # in KB

print(f"n={num}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
