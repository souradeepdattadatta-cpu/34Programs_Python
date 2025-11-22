''' question-31:- Implement the probabilistic Miller-Rabin test is_prime_miller_rabin(n, k) with k rounds'''

import time
import tracemalloc
import random

def miller_rabin_test(d, n):
    a = random.randint(2, n - 2)
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False

def is_prime_miller_rabin(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for _ in range(k):
        if not miller_rabin_test(d, n):
            return False
    return True

n = 101
k = 5  # Number of rounds

tracemalloc.start()
start_time = time.time()
result = is_prime_miller_rabin(n, k)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"n={n}, k={k}, result={result}, time_taken_sec={end_time - start_time:.8f}, memory_utilized_KB={peak / 1024:.3f}")
