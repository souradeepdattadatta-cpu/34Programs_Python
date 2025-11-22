'''question-20:- Write a function for Modular Exponentiation mod_exp(base, exponent, modulus) that efficiently calculates (baseᵉˣᵖᵒⁿᵉⁿᵗ) % modulus.'''  

import time
import tracemalloc

def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

base = 5
exponent = 117
modulus = 19

tracemalloc.start()
start_time = time.time()
result = mod_exp(base, exponent, modulus)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_utilized = peak / 1024  # in KB

print(f"base={base}, exponent={exponent}, modulus={modulus}, result={result}, time_taken_sec={time_taken:.8f}, memory_utilized_KB={memory_utilized:.3f}")
