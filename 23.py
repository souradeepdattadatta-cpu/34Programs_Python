''' question-23:-Write a function Quadratic Residue Check is_quadratic_residue(a, p) that checks if x² ≡ a mod p has a solution'''

import time
import tracemalloc

def legendre_symbol(a, p):
    return pow(a, (p - 1) // 2, p)

def is_quadratic_residue(a, p):
    if a == 0:
        return True
    ls = legendre_symbol(a, p)
    if ls == 1:
        return True
    elif ls == p - 1:
        return False
    else:
        return False

# Example input
a = 10
p = 13

tracemalloc.start()
start_time = time.time()
result = is_quadratic_residue(a, p)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024  # in KB

print(f"a={a}, p={p}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
