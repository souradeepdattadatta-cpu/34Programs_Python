''' question-32:- Implement pollard_rho(n) for integer factorization using Pollard's rho algorithm'''

import time
import tracemalloc
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    x = 2
    y = 2
    d = 1
    f = lambda x: (x * x + 1) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    if d == n:
        return None
    return d

num = 8051  # Example input

tracemalloc.start()
start_time = time.time()
result = pollard_rho(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"n={num}, factor={result}, time_taken_sec={end_time - start_time:.8f}, memory_utilized_KB={peak / 1024:.3f}")
