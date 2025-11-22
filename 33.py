''' question-33:- Write a function zeta_approx(s, terms) that approximates the Riemann zeta function ζ(s) using the first 'terms' of the series'''

import time
import tracemalloc

def zeta_approx(s, terms):
    total = 0
    for n in range(1, terms + 1):
        total += 1 / (n ** s)
    return total

s = 2  # Example input
terms = 100000  # Number of terms in approximation

tracemalloc.start()
start_time = time.time()
result = zeta_approx(s, terms)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"s={s}, terms={terms}, zeta_approx={result}, time_taken_sec={end_time - start_time:.8f}, memory_utilized_KB={peak / 1024:.3f}")
