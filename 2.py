'''question-2:- Write a function is_palindrome(n) that checks if a number reads the same forwards and backwards.'''

import time
import tracemalloc

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

num = 12321

tracemalloc.start()
start_time = time.time()
result = is_palindrome(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024

print(f"n={num}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
