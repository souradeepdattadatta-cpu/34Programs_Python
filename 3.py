'''question-3:-Write a function mean_of_digits(n) that returns the average of all digits in a number'''

import time
import tracemalloc

def mean_of_digits(n):
    digits = [int(d) for d in str(n)]
    return sum(digits) / len(digits) if digits else 0

num = 12345

tracemalloc.start()
start_time = time.time()
result = mean_of_digits(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024

print(f"n={num}, result={result:.5f}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
