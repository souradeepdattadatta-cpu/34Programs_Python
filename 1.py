'''question-1:-Write a function factorial(n) that calculates the factorial of a non-negative integer n (n!).'''
import time
import tracemalloc

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

n = 10

tracemalloc.start()
start_time = time.time()
result = factorial(n)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak/1024 

print(f"n={n}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
