from functools import lru_cache

def fib_exponential(n):
    """
    Naive recursive Fibonacci implementation.
    Time Complexity: O(2^n) (more precisely Θ(ϕ^n)), because it recomputes overlapping subproblems.
    Space Complexity: O(n) due to recursion depth.
    -> Classic example of inefficiency without dynamic programming.
    """
    if n < 2:
        return n
    return fib_exponential(n - 1) + fib_exponential(n - 2)

# Improved version using memoization
@lru_cache(maxsize=None)
def fib_linear(n):
    """
    Fibonacci with memoization (top-down dynamic programming).
    Time Complexity: O(n)
    Space Complexity: O(n) for cache + recursion stack.
    """
    if n < 2:
        return n
    return fib_linear(n - 1) + fib_linear(n - 2)

# Example usage:
print(fib_exponential(10))  # slow for large n
print(fib_linear(40))       # fast thanks to memoization
