''' question-30:- Write a function Carmichael Number Check is_carmichael(n) that checks if a composite number n satisfies aⁿ⁻¹ ≡ 1 mod n for all a coprime to n.'''

import time
import tracemalloc
import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def is_carmichael(n):
    if n < 2 or is_prime(n):
        return False
    for a in range(2, n):
        if gcd(a, n) == 1:
            if mod_exp(a, n - 1, n) != 1:
                return False
    return True

num = 561  # Example Carmichael number

tracemalloc.start()
start_time = time.time()
result = is_carmichael(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"n={num}, result={result}, time_taken_sec={end_time - start_time:.8f}, memory_utilized_KB={peak / 1024:.3f}")
