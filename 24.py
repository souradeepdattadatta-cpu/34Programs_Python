''' question-24:-Write a function order_mod(a, n) that finds the smallest positive integer k such that aᵏ ≡ 1 mod n.'''

import time
import tracemalloc

def order_mod(a, n):
    if n == 1:
        return 0
    k = 1
    val = a % n
    while val != 1:
        val = (val * a) % n
        k += 1
        if k > n:  # safeguard to avoid infinite loop
            return -1
    return k

# Example input
a = 2
n = 7

tracemalloc.start()
start_time = time.time()
result = order_mod(a, n)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024  # in KB

print(f"a={a}, n={n}, order={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
