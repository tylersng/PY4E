import time
start_time = time.time()

def fib(n):
    if n == 1 or n == 2:
        return 1 
    else:
        return fib(n-1) + fib(n-2)
print(fib(5))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time}.4f seconds")
#time complexity: O(2^n)