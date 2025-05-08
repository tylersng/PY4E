import time
start_time = time.time()
def fib(n, memo):
    if memo[n] is not None:
        print(memo[n])
        return memo[n]
    if n == 1 or n == 2:
        return 1
    else:
        result = fib(n-1, memo) + fib(n-2, memo)
        memo[n] = result
        return result 
n = 5 
memo = [None] * (n+1)
print(fib(n, memo))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time}.4f seconds")
#time complexity: O(2n + 1) = O(n)