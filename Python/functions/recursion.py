def fib(n):
    # base case of the recursion
    if(n == 0 or n == 1):
        return n
    
    return fib(n-2) + fib(n-1)
print(fib(10))