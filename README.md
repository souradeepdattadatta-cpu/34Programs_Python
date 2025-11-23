# 34Programs_Python
College Assignment - Python Algorithms & Number Theory

This repository contains a collection of Python scripts developed for a college assignment. Each script implements a specific mathematical algorithm or number theory problem, complete with performance profiling to measure execution time and memory usage.

Overview

The project focuses on implementing efficient algorithms for various number theory problems, ranging from basic digit manipulation to complex cryptographic functions like Pollard's Rho and the Chinese Remainder Theorem.

Key Features:

Language: Python 3.11+

Performance Tracking: Every script utilizes time and tracemalloc to report:

Execution Time (seconds)

Memory Usage (KB)

Standard Library: Uses only standard Python libraries (math, time, tracemalloc).

List of Programs

The repository includes solutions for the following problems:

Basic Number Properties

Factorial: Calculates n! for non-negative integers.

Palindrome Check: Determines if a number reads the same forwards and backwards.

Mean of Digits: Calculates the average value of all digits in a number.

Digital Root: Recursive sum of digits until a single-digit result is found.

Amicable Pairs: Checks if two numbers are amicable (each is the sum of the other's proper divisors).

Number Classification

Abundant Number: Checks if the sum of proper divisors > n.

Deficient Number: Checks if the sum of proper divisors < n.

Harshad Number: Checks if a number is divisible by the sum of its digits.

Automorphic Number: Checks if n^2 ends with the digits of n.

Pronic Number: Checks if n is the product of two consecutive integers (n = x(x+1)).

Perfect Power: Checks if n can be expressed as a^b.

Highly Composite Number: Checks if a number has more divisors than any smaller positive integer.

Polygonal Numbers: Generates the n-th s-gonal number.

Primes & Factors

Prime Factors: Returns a list of all prime factors.

Count Distinct Prime Factors: Counts unique prime factors.

Prime Power: Checks if n = p^k where p is prime.

Mersenne Prime: Checks if a number is a prime of the form 2^p - 1.

Twin Primes: Finds pairs of primes (p, p+2) up to a limit.

Fibonacci Prime: Checks if a number is both a Fibonacci number and prime.

Pollard's Rho Algorithm: Implements integer factorization.

Sequences & Series

Lucas Sequence: Generates the Lucas sequence (similar to Fibonacci but starts with 2, 1).

Collatz Sequence: Calculates the stopping time (steps to reach 1).

Partition Function: Calculates the number of ways to write n as a sum of positive integers.

Zeta Function: Approximates the Riemann Zeta function.

Multiplicative Persistence: Counts how many times digits must be multiplied to reach a single digit.

Modular Arithmetic & Cryptography

Modular Exponentiation: Efficiently computes (base^exponent) % modulus.

Modular Multiplicative Inverse: Finds x such that ax = 1 (mod m).

Chinese Remainder Theorem: Solves a system of congruences.

Quadratic Residue: Checks if a is a quadratic residue modulo p (using Legendre Symbol).

Order Modulo n: Finds the smallest k such that a^k = 1 (mod n).

Carmichael Function: Computes lambda(n).

Requirements

Python 3.x (Tested on Python 3.11.4)

OS: Windows/Linux/macOS

Author

Souradeep Datta

Course Code: CSE1021

Registration Number: 25BAI10732

