'''question-26:- Write a function Lucas Numbers Generator lucas_sequence(n) that generates the first n Lucas numbers (similar to Fibonacci but starts with 2, 1).'''

import time
import tracemalloc

def lucas_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [2]
    sequence = [2, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

num = 10  # Example input

tracemalloc.start()
start_time = time.time()
result = lucas_sequence(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024  # in KB

print(f"n={num}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
