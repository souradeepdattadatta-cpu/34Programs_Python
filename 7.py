'''question:7:-Write a function for harshad number is_harshad(n) that checks if a number is divisible by the sum of its digits.'''


import time
import tracemalloc

def is_harshad(n):
    digits_sum = sum(int(d) for d in str(n))
    return n % digits_sum == 0

num = 18

tracemalloc.start()
start_time = time.time()
result = is_harshad(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024

print(f"n={num}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")







